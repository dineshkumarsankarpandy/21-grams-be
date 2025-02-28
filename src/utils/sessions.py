from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.core.config import settings
from typing import AsyncGenerator
from src.utils.logging import logging

# Set up logging
logger = logging.getLogger(__name__)

DATABASE_URL = settings.DATABASE_URL  # e.g. "postgresql+asyncpg://user:pass@localhost:5432/mydb"
 
engine = create_async_engine(
    DATABASE_URL,
    echo=True,             
    pool_size=5,
    max_overflow=10,        
    pool_timeout=30,        
)
 
SessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,  # Corrected syntax error by replacing 'class =' with 'class_='
    expire_on_commit=False
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Error in database session: {e}")
            raise

Base = declarative_base()