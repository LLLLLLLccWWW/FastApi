from fastapi import APIRouter

router = APIRouter()

# @router.get("/data/{data_id}")
# async def root(data_id):
#     return {"message": f"Hello data {data_id}"}

@router.post("")
async def root():
    return {"message": "Hello current data"}