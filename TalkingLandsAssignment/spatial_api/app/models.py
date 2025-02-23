from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry  # PostGIS extension for SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PointLocation(Base):
    """
    Table to store point-based location data (latitude, longitude).
    """
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    coordinates = Column(Geometry("POINT"), nullable=False)  # Geo field for points


class PolygonArea(Base):
    """
    Table to store polygon data (regions, zones).
    """
    __tablename__ = "polygons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    boundary = Column(Geometry("POLYGON"), nullable=False)  # Geo field for polygons
