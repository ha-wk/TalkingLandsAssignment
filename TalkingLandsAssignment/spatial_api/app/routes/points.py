from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_point
from app.schemas import PointCreate

router = APIRouter()

def get_db():
    """
    Dependency function to get the database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/points/")
def add_point(point: PointCreate, db: Session = Depends(get_db)):
    """
    API to add a new point location.
    """
    return create_point(db, point.name, point.latitude, point.longitude)
