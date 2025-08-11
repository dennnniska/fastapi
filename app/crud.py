from sqlalchemy.orm import Session
import models, schemas

def get_entry(db: Session, entry_id: int):
    return db.query(models.DiaryEntry).filter(models.DiaryEntry.id == entry_id).first()

def get_entries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.DiaryEntry).offset(skip).limit(limit).all()

def create_entry(db: Session, entry: schemas.DiaryEntryCreate):
    db_entry = models.DiaryEntry(title=entry.title, content=entry.content)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

def update_entry(db: Session, entry_id: int, entry: schemas.DiaryEntryUpdate):
    db_entry = get_entry(db, entry_id)
    if db_entry is None:
        return None
    
    if entry.title is not None:
        db_entry.title = entry.title
    if entry.content is not None:
        db_entry.content = entry.content
    if entry.is_completed is not None:
        db_entry.is_completed = entry.is_completed
    
    db.commit()
    db.refresh(db_entry)
    return db_entry

def delete_entry(db: Session, entry_id: int):
    db_entry = get_entry(db, entry_id)
    if db_entry is None:
        return None
    
    db.delete(db_entry)
    db.commit()
    return db_entry

def mark_entry_completed(db: Session, entry_id: int, completed: bool = True):
    db_entry = get_entry(db, entry_id)
    if db_entry is None:
        return None
    
    db_entry.is_completed = completed
    db.commit()
    db.refresh(db_entry)
    return db_entry