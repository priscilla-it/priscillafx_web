"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from database.db import async_engine
from database.models.auth import User
from database.models.custom import Custom
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi_cache.decorator import cache
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from icecream import ic
from ..auth.config import current_superuser


custom_router = APIRouter(prefix='/custom', tags=['Custom'])


@custom_router.get('/get_custom')
@cache(expire=60, namespace='all_custom')
async def get_custom():
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Custom)
            results = await session.exec(statement)
            customs = [custom for custom in results]
            if not customs:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No custom found',
                }
            return {
                'status': 'Success',
                'data': customs,
                'details': 'Custom found',
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                'status': 'Error',
                'data': None,
                'details': 'Server-side error',
            },
        )
        ic('❌ [ERROR] get_custom: ', e)


@custom_router.post('/add_custom')
async def add_custom(
    user: User = Depends(current_superuser),
    name: str = Form(),
    description: str = Form(),
    price: str = Form(),
    image_url: str = Form(),
):
    new_custom = Custom(
        name=name, description=description, price=price, image_url=image_url
    )

    try:
        async with AsyncSession(async_engine) as session:
            session.add(new_custom)

            await session.commit()
            await session.refresh(new_custom)

            if new_custom.id is not None:
                return {
                    'status': 'Success',
                    'data': {'id': new_custom.id},
                    'message': 'Custom added successfully',
                }
            return {
                'status': 'Error',
                'data': None,
                'message': 'Custom has not been added',
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                'status': 'Error',
                'data': None,
                'details': 'Server-side error',
            },
        )
        ic('❌ [ERROR] add_custom: ', e)


@custom_router.post('/delete_custom')
async def delete_custom(
    user: User = Depends(current_superuser), id: int = Form()
):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Custom).where(Custom.id == id)
            results = await session.exec(statement)
            artist = results.one()

            await session.delete(artist)
            await session.commit()

            if artist is None:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No custom for delete',
                }
            return {
                'status': 'Success',
                'data': artist,
                'details': 'Custom was deleted',
            }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                'status': 'Error',
                'data': None,
                'details': 'Server-side error',
            },
        )
        ic('❌ [ERROR] delete_custom: ', e)
