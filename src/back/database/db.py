"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from typing import Any, AsyncGenerator
from sqlmodel import SQLModel
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncAttrs,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from ..config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from ..logger import logger


DATABASE_URL = (
    f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async_engine = create_async_engine(DATABASE_URL, echo=False)
async_session = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, Any]:
    """Получить сеанс работы с базой данных.
    Будет использоваться для внедрения зависимостей.
    """
    async with async_session() as session, session.begin():
        yield session


async def init_models() -> None:
    """Создаёт таблицы, если они ещё не существуют."""
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            await conn.run_sync(SQLModel.metadata.create_all)
            # await conn.run_sync(SQLModel.metadata.drop_all)
    except ConnectionRefusedError as e:
        logger.error('❌ [ERROR] database: ', e)
