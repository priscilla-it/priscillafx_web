"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from datetime import datetime
from ..db import Base, async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    JSON,
    TIMESTAMP,
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)


async def add_predefined_roles():
    async with AsyncSession(async_engine) as session:
        roles = [
            {
                'name': 'superadmin',
                'permissions': {'manage_users': True, 'manage_roles': True},
            },
            {'name': 'user', 'permissions': {'view_content': True}},
        ]

        for role in roles:
            new_role = Role(name=role['name'], permissions=role['permissions'])
            session.add(new_role)

        await session.commit()


class Role(Base):
    __tablename__ = 'Role'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.now())
    role_id = Column(Integer, ForeignKey(Role.id))
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
