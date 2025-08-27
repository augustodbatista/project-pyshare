from .database import Base
from sqlalchemy import Column, String, BigInteger, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Share(Base):
    __tablename__ = "shares"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    original_filename = Column(String)
    storage_key = Column(String, unique=True, index=True)
    file_size = Column(BigInteger)
    mime_type = Column(String)
    created_at = Column(DateTime)
    expires_at = Column(DateTime)
