from fastapi import FastAPI

from app.routes import router


def init_routers(application: FastAPI):
    application.include_router(router)


def create_app():
    _app = FastAPI(title="KINO GO")
    init_routers(_app)
    return _app


app = create_app()
