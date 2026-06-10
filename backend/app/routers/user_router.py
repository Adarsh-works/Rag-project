from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.repositories.user_repositories import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
async def create_user(user: UserCreate):

    user_id = await UserRepository.create_user(
        user.model_dump()
    )

    return {
        "message": "User created successfully",
        "user_id": user_id
    }


@router.get("/")
async def get_users():

    users = await UserRepository.get_all_users()

    return users