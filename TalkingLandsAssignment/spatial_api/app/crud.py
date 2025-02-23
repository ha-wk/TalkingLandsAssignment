from sqlalchemy.orm import Session
from app.models import PointLocation, PolygonArea
from geoalchemy2.shape import from_shape
from shapely.geometry import Point, Polygon

def create_point(db: Session, name: str, latitude: float, longitude: float):
    """
    Store a new point location in the database.
    """
    geo_point = from_shape(Point(longitude, latitude), srid=4326)  # Convert to PostGIS format
    point = PointLocation(name=name, coordinates=geo_point)
    db.add(point)
    db.commit()
    db.refresh(point)
    return point


def create_polygon(db: Session, name: str, coordinates: list):
    """
    Store a new polygon region in the database.
    """
    geo_polygon = from_shape(Polygon(coordinates), srid=4326)  # Convert to PostGIS format
    polygon = PolygonArea(name=name, boundary=geo_polygon)
    db.add(polygon)
    db.commit()
    db.refresh(polygon)
    return polygon
