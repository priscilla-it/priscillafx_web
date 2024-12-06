"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from database.db import async_engine
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi_cache.decorator import cache
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from icecream import ic
from database.models.artists import Artists
from database.models.auth import User
from ..auth.config import current_superuser


artists_router = APIRouter(prefix='/artists', tags=['Artists'])


@artists_router.get('/get_artists')
@cache(expire=60, namespace='get_artists')
async def get_artists():
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Artists)
            results = await session.exec(statement)
            artists = [artist for artist in results]
            if not artists:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No artists found',
                }
            return {
                'status': 'Success',
                'data': artists,
                'details': 'Artists found',
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
        ic('❌ [ERROR] get_artists:', e)


@artists_router.post('/add_artist')
async def add_artist(
    user: User = Depends(current_superuser),
    image_url: str = Form(),
    full_name: str = Form(),
    band: str = Form(),
    link: str = Form(''),
):
    new_artist = Artists(
        image_url=image_url, full_name=full_name, band=band, link=link
    )

    try:
        async with AsyncSession(async_engine) as session:
            session.add(new_artist)

            await session.commit()
            await session.refresh(new_artist)

            if new_artist.id is not None:
                return {
                    'status': 'Success',
                    'data': {'id': new_artist.id},
                    'message': 'Artist added successfully',
                }
            return {
                'status': 'Error',
                'data': None,
                'message': 'Artist has not been added',
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
        ic('❌ [ERROR] add_artist: ', e)


@artists_router.post('/delete_artist')
async def delete_artist(
    user: User = Depends(current_superuser), id: int = Form()
):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Artists).where(Artists.id == id)
            results = await session.exec(statement)
            artist = results.one()

            await session.delete(artist)
            await session.commit()

            if artist is None:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No artist for delete',
                }
            return {
                'status': 'Success',
                'data': artist,
                'details': 'Artist was deleted',
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
        ic('❌ [ERROR] delete_artist: ', e)
