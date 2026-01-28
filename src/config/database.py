from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# SQLite 비동기 URL 설정
DATABASE_URL = "sqlite+aiosqlite:///./kapi.db"

# 엔진 생성
engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# 세션 팩토리 생성
async_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

# 베이스 모델 클래스
class Base(DeclarativeBase):
    pass

# Dependency injection을 위한 세션 생성기
async def get_db():
    async with async_session() as session:
        yield session