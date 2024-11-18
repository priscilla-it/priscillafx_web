"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from fastapi import APIRouter
from ..auth.config import auth_backend, fastapi_users
from ..auth.schemas import UserCreate, UserRead


auth_router = APIRouter(prefix='/auth', tags=['Auth'])


auth_router.include_router(fastapi_users.get_auth_router(auth_backend))
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)
