from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.core.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(200))
    email = Column(String(200), unique=True, nullable=False)
    password = Column(String(200))
    role = Column(Enum("admin","customer", name="user_roles"), default="customer")
    created_at = Column(DateTime, default=datetime.utcnow)
