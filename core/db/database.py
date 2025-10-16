# app/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Create database engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class for our models
Base = declarative_base()

# Dependency for getting DB session (used in routes)
async def get_db():
    async with async_session() as session:
        yield session
