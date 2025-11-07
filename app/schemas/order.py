from pydantic import BaseModel
from uuid import UUID
from typing import List
from decimal import Decimal
from datetime import datetime

class OrderItemBase(BaseModel):
    product_id: UUID
    quantity: int
    price: Decimal

class OrderCreate(BaseModel):
    user_id: UUID
    items: List[OrderItemBase]
    payment_method: str

class OrderItemRead(OrderItemBase):
    id: UUID

    class Config:
        orm_mode = True

class OrderRead(BaseModel):
    id: UUID
    user_id: UUID
    status: str
    total: Decimal
    payment_method: str
    payment_status: str
    items: List[OrderItemRead]
    created_at: datetime

    class Config:
        from_attributes  = True
