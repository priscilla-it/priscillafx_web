"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from database.db import get_async_session
from database.models.auth import User
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
