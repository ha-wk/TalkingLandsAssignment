from pydantic import BaseModel
from typing import List

class PointCreate(BaseModel):
    """
    Schema for creating a point (latitude, longitude).
    """
    name: str
    latitude: float
    longitude: float


class PolygonCreate(BaseModel):
    """
    Schema for creating a polygon with a list of coordinate points.
    """
    name: str
    coordinates: List[List[float]]  # A list of (lat, long) pairs
