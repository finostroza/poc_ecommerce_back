from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.core.db import Base
import uuid

class StoreConfig(Base):
    __tablename__ = "store_config"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    store_name = Column(String(100))
    logo_url = Column(String(500))
    theme = Column(JSON)  # {"primary_color": "#123456"}
    currency = Column(String(10), default="CLP")
    contact_email = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow)
