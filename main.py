from fastapi import FastAPI,Form  
from routers.api_v1.routers import router

app = FastAPI()
app.include_router(router, prefix="/api/v1")

# fake_items_db = [{"item_name": "Item 1"}, {"item_name": "Item 2"}, {"item_name": "Item 3"}]

# @app.get("/users/{user_id}")
# async def root(user_id):
#     return {"message":f"Hello {user_id}"}

# @app.get("/items/")
# async def read_item(skip: int = 0, limit :int = 10):
#     return fake_items_db[skip: skip+limit]

# @app.post("/login")
# async def login(username: str = Form(), password: str = Form()):
#     return {"username": username, "password": password}