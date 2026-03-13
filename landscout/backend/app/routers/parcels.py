from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.parcel import Parcel, ParcelScore

router = APIRouter()

@router.get("/")
async def get_parcels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    parcels = db.query(Parcel).offset(skip).limit(limit).all()
    return {"parcels": [{"id": p.id, "address": p.address, "city": p.city} for p in parcels]}

@router.get("/{parcel_id}")
async def get_parcel(parcel_id: int, db: Session = Depends(get_db)):
    parcel = db.query(Parcel).filter(Parcel.id == parcel_id).first()
    if not parcel:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return {"parcel": parcel}
