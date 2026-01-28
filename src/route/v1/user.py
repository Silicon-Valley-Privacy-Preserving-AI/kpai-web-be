from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.database import get_db
from src.service.user_service import UserService
from src.schema.user import UserCreate, UserResponse
from fastapi import status

router = APIRouter(prefix="/users", tags=["User"])

async def get_user_service(db: AsyncSession = Depends(get_db)):
    return UserService(db)

@router.post("",
             summary="Create new user (Register)",
             response_model=UserResponse,
             status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.create_user(user_data)

@router.get("", summary="Get user list")
async def get_users(
    user_service: UserService = Depends(get_user_service)
):
    return await user_service.get_users()