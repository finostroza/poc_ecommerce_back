from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.core.db import Base

class ProductCategory(Base):
    __tablename__ = "product_category"

    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), primary_key=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey("categories.id"), primary_key=True)
