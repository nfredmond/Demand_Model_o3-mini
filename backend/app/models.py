from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from app.database import Base

class Zone(Base):
    __tablename__ = "zones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    geometry = Column(Geometry("POLYGON", srid=4326))

class Road(Base):
    __tablename__ = "roads"
    id = Column(Integer, primary_key=True, index=True)
    geometry = Column(Geometry("LINESTRING", srid=4326))
    capacity = Column(Float)

class Demographic(Base):
    __tablename__ = "demographics"
    id = Column(Integer, primary_key=True, index=True)
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=False)
    population = Column(Integer)
    employment = Column(Integer)

class TripMatrix(Base):
    __tablename__ = "trip_matrices"
    id = Column(Integer, primary_key=True, index=True)
    origin_zone_id = Column(Integer, ForeignKey("zones.id"))
    dest_zone_id = Column(Integer, ForeignKey("zones.id"))
    trips = Column(Float)
