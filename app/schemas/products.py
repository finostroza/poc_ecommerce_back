from pydantic import BaseModel
from typing import Optional, Dict
from decimal import Decimal
from uuid import UUID
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    stock: int = 0
    image_url: Optional[str] = None
    is_active: bool = True
    attributes: Optional[Dict] = None

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes  = True
