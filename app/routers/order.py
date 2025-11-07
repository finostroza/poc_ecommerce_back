from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate, OrderRead
from app.core.db import get_db
import uuid
from datetime import datetime

router = APIRouter()

# Crear orden
@router.post("/", response_model=OrderRead)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(
        user_id=order.user_id,
        status="pending",
        total=sum([item.price * item.quantity for item in order.items]),
        payment_method=order.payment_method,
        payment_status="pending",
        created_at=datetime.utcnow(),
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # Agregar items
    for item in order.items:
        db_item = OrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(db_item)
    db.commit()
    return db_order

# Listar órdenes
@router.get("/", response_model=List[OrderRead])
def list_orders(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return db.query(Order).offset(skip).limit(limit).all()

# Obtener orden por id
@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: str, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
