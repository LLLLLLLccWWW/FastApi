from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()

class User(BaseModel):
    age: int
    name: str
    email: str

class UserDetail(BaseModel):
    name: str
    age: int
    email: str
    phone: str

fake_db = [
    UserDetail(name="John Doe4", age=30, email="222@example.com", phone="123-456-7890"),
    UserDetail(name="Jane Doe3", age=25, email="333@example.com", phone="987-654-3210"),
    UserDetail(name="John Doe2", age=31, email="111@example.com", phone="123-456-5555"),
    UserDetail(name="Jane Doe1", age=11, email="355@example.com", phone="555-555-5555"),
]
@router.get("",tags=["ithome"])
async def get_user() -> list[User]:
    return fake_db

@router.get("/admin",tags=["ithome"])
async def get_users() -> list[UserDetail]:
    return fake_db

@router.post("")
async def create_user() -> User:
    return User