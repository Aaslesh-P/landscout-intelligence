from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_watchlist():
    return {"message": "Watchlist feature coming soon!"}
