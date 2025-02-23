from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_polygon
from app.schemas import PolygonCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/polygons/")
def add_polygon(polygon: PolygonCreate, db: Session = Depends(get_db)):
    """
    API to add a new polygon region.
    """
    return create_polygon(db, polygon.name, polygon.coordinates)
