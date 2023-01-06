import uvicorn
from fastapi import FastAPI

from app import db
from app.config import settings
from app.api.v1.urls import api_router

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.SERVICE_NAME,
    docs_url='/docs' if settings.SHOW_DOCS else None,
    openapi_url='/openapi.json'
)

app.include_router(api_router, prefix='/api')


@app.on_event('startup')
async def on_startup():
    db.init(settings)

if __name__ == "__main__":
    uvicorn.run('main:app', host=settings.SERVICE_HOST,
                port=settings.SERVICE_PORT)
