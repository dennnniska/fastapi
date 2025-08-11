from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DiaryEntryBase(BaseModel):
    title: str
    content: Optional[str] = None

class DiaryEntryCreate(DiaryEntryBase):
    pass

class DiaryEntryUpdate(DiaryEntryBase):
    is_completed: Optional[bool] = None

class DiaryEntry(DiaryEntryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    is_completed: bool

    class Config:
        from_attributes = True