"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

from database.db import async_engine
from database.models.auth import User
from database.models.blog import Blog
from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi_cache.decorator import cache
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from icecream import ic
from ..auth.config import current_superuser


blog_router = APIRouter(prefix='/blog', tags=['Blog'])


@blog_router.get('/get_posts')
@cache(expire=60, namespace='get_posts')
async def get_posts():
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Blog)
            results = await session.exec(statement)
            posts = [post for post in results]
            if not posts:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No posts found',
                }
            return {
                'status': 'Success',
                'data': posts,
                'details': 'Posts found',
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
        ic('❌ [ERROR] get_posts: ', e)


@blog_router.post('/add_post')
async def add_post(
    user: User = Depends(current_superuser),
    title: str = Form(),
    content: str = Form(),
    image_url: str = Form(""),
    file_url: str = Form(""),
):
    new_post = Blog(
        title=title, content=content, image_url=image_url, file_url=file_url
    )

    try:
        async with AsyncSession(async_engine) as session:
            session.add(new_post)

            await session.commit()
            await session.refresh(new_post)

            if new_post.id is not None:
                return {
                    'status': 'Success',
                    'data': {'id': new_post.id},
                    'message': 'Post added successfully',
                }
            return {
                'status': 'Error',
                'data': None,
                'message': 'Post has not been added',
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
        ic('❌ [ERROR] add_post: ', e)


@blog_router.post('/delete_post')
async def delete_post(
    user: User = Depends(current_superuser), id: int = Form()
):
    try:
        async with AsyncSession(async_engine) as session:
            statement = select(Blog).where(Blog.id == id)
            results = await session.exec(statement)
            blog = results.one()

            await session.delete(blog)
            await session.commit()

            if blog is None:
                return {
                    'status': 'Info',
                    'data': None,
                    'details': 'No post for delete',
                }
            return {
                'status': 'Success',
                'data': blog,
                'details': 'Post was deleted',
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
        ic('❌ [ERROR] delete_post: ', e)
