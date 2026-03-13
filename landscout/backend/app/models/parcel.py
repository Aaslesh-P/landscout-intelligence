from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, Text
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
from app.database import Base

class Parcel(Base):
    __tablename__ = "parcels"
    id = Column(Integer, primary_key=True, index=True)
    parcel_id = Column(String(100), unique=True, nullable=False)
    address = Column(Text)
    city = Column(String(100))
    state = Column(String(2))
    latitude = Column(Numeric(10, 8))
    longitude = Column(Numeric(11, 8))
    geom = Column(Geometry('POINT', srid=4326))
    lot_size_acres = Column(Numeric(10, 2))
    is_for_sale = Column(Boolean, default=False)
    asking_price = Column(Numeric(12, 2))

class ParcelScore(Base):
    __tablename__ = "parcel_scores"
    id = Column(Integer, primary_key=True)
    parcel_id = Column(Integer, nullable=False)
    total_score = Column(Numeric(5, 2))
    growth_score = Column(Numeric(5, 2))
    infrastructure_score = Column(Numeric(5, 2))
    calculated_at = Column(DateTime(timezone=True), server_default=func.now())
