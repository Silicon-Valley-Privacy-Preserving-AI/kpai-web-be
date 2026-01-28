from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.model.user import User
from src.schema.user import UserCreateRequest, UserModifyRequest
from src.util.security import get_password_hash

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreateRequest):
        new_user = User(
            email=user_data.email,
            username=user_data.username,
            password=get_password_hash(user_data.password)
        )
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def delete_user(self, user: User):
        await self.db.delete(user)
        await self.db.commit()
        return {"message": "User deleted successfully"}

    async def get_user_by_email(self, email: str):
        result = await self.db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def modify_user(self, user: User, user_data: UserModifyRequest):
        if user_data.email is not None:
            user.email = user_data.email

        if user_data.username is not None:
            user.username = user_data.username

        await self.db.commit()
        await self.db.refresh(user)

        return {"message": "User modified successfully"}