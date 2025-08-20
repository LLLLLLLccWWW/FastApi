from fastapi import APIRouter
router = APIRouter()

@router.get("/{user_id}",tags=["ithome"])
async def get_user(user_id):
    return {"message": f"Hello user {user_id}"}

@router.post("")
async def create_user():
    return {"message": "Hello current user"}