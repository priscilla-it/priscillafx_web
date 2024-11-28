"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from icecream import ic
from logger import logger
from config import REDIS_HOST, REDIS_PORT
from api.routers.artist.router import artist_router
from api.routers.auth.router import auth_router
from api.routers.blog.router import blog_router
from api.routers.custom.router import custom_router
from api.routers.tasks.router import tasks_router


# Startup events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # FastAPI
    try:
        ic('✅ [START]: API')
    except Exception as e:
        logger.error('❌ [ERROR] FastAPI: ', e)

    # Redis
    try:
        redis = aioredis.from_url(
            f'redis://{REDIS_HOST}:{REDIS_PORT}',
            encoding='utf8',
            decode_responses=True,
        )
        FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')
        ic('✅ [START]: Redis')
    except Exception as e:
        logger.error('❌ [ERROR] Redis: ', e)

    yield


# FastAPI initialize
app = FastAPI(
    lifespan=lifespan,
    title='Priscilla Fx',
    redoc_url=None,
    # docs_url=None,
    # openapi_url=None,
)

# Routers
app.include_router(auth_router)
app.include_router(blog_router)
app.include_router(custom_router)
app.include_router(artist_router)
app.include_router(tasks_router)


# Mount static files
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app.mount('/static', StaticFiles(directory=static_dir), name='static')


# Favicon
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=204)  # No Content


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:50160',  # Next.js local port
        # TODO 'http://localhost', VDS IP
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=[
        'Content-Type',
        'Set-Cookie',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Authorization',
    ],
)

if __name__ == '__main__':
    import uvicorn

    try:
        uvicorn.run(
            app, host='localhost', port=50150, log_level='info', lifespan='on'
        )
    except Exception as e:
        ic('[ERROR] uvicorn: ', e)
