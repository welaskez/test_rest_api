from api import router
from core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    """
    Initialize FastAPI application instance
    :return: fastapi app
    """
    app = FastAPI()

    app.include_router(router)

    app.add_middleware(
        middleware_class=CORSMiddleware,  # type: ignore
        allow_origins=settings.cors.allowed_origins,
        allow_credentials=settings.cors.allow_credentials,
        allow_methods=settings.cors.allowed_methods,
        allow_headers=settings.cors.allowed_headers,
    )

    return app
