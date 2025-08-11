from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class DiaryEntry(Base):
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_completed = Column(Boolean, default=False)