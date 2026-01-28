from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.model.user import User
from src.schema.user import UserCreate

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreate):
        new_user = User(
            email=user_data.email,
            username=user_data.username,
            password=user_data.password
        )
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        return new_user

    async def get_users(self):
        result = await self.db.execute(select(User))
        return result.scalars().all()