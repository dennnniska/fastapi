from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud, models
from database import engine, get_db, Base
from typing import List
import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/entries/", response_model=schemas.DiaryEntry)
def create_entry(entry: schemas.DiaryEntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(db=db, entry=entry)

@app.get("/entries/", response_model=List[schemas.DiaryEntry])
def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = crud.get_entries(db, skip=skip, limit=limit)
    return entries

@app.get("/entries/{entry_id}", response_model=schemas.DiaryEntry)
def read_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = crud.get_entry(db, entry_id=entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@app.put("/entries/{entry_id}", response_model=schemas.DiaryEntry)
def update_entry(entry_id: int, entry: schemas.DiaryEntryUpdate, db: Session = Depends(get_db)):
    db_entry = crud.update_entry(db=db, entry_id=entry_id, entry=entry)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@app.delete("/entries/{entry_id}", response_model=schemas.DiaryEntry)
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    db_entry = crud.delete_entry(db=db, entry_id=entry_id)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

@app.patch("/entries/{entry_id}/complete", response_model=schemas.DiaryEntry)
def mark_entry_completed(entry_id: int, completed: bool = True, db: Session = Depends(get_db)):
    db_entry = crud.mark_entry_completed(db=db, entry_id=entry_id, completed=completed)
    if db_entry is None:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry

if __name__ == "__main__":
    uvicorn.run("main:app")