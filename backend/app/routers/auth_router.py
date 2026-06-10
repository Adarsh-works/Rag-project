from fastapi import (
    APIRouter,
    HTTPException
)

from app.schemas.user_schema import UserCreate
from app.schemas.auth_schema import LoginRequest

from app.repositories.user_repositories import UserRepository

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
async def register(user: UserCreate):

    existing_user = await UserRepository.get_by_email(
        user.email
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user_data = user.model_dump()

    user_data["password"] = hash_password(
        user.password
    )

    user_id = await UserRepository.create_user(
        user_data
    )

    return {
        "message": "User registered successfully",
        "user_id": user_id
    }

@router.post("/login")
async def login(user: LoginRequest):

    db_user = await UserRepository.get_by_email(
        user.email
    )

    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        user.password,
        db_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "sub": str(db_user["_id"])
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/logout")
async def logout():
    return {
        "message": "Logged out successfully"
    }

