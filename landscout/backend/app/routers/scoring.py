from fastapi import APIRouter
router = APIRouter()

@router.post("/calculate/{parcel_id}")
async def calculate_score(parcel_id: int):
    return {"message": "Scoring engine coming soon!", "parcel_id": parcel_id}
