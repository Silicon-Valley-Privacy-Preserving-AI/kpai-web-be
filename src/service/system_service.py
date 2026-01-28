from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.model.user import User

class SystemService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def healthcheck(self):
        return {"message": "yes"}

    async def get_users(self):
        result = await self.db.execute(select(User))
        return result.scalars().all()