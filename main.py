from fastapi import FastAPI,Form  
from routers.api_v1.routers import router
from config import Settings

app = FastAPI(root_path="/ithome")
app.include_router(router, prefix="/api/v1")

@app.get("/app")
def read_main():
    return {"message": "Hello from main app"}

subapi = FastAPI()
@subapi.get("/sub")
def read_sub():
    return {"message": "Hello from sub API"}

app.mount("/subapi",subapi)

settings = Settings()
@app.get("/info")
async def get_info():
    return{
        "app_name": settings.app_name,
        "version": settings.version,
        "description": settings.description
    }

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