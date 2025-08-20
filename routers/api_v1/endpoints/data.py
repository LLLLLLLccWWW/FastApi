from fastapi import APIRouter

router = APIRouter()

@router.get("",summary="Get Data", description="This is a short description")
async def get_data():
    return {"message": "Hello data"}

@router.post("",deprecated=True)
async def create_data():
    return {"message": "Hello current data"}