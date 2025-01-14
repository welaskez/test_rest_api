from api import router
from core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse


def create_app():
    app = FastAPI(default_response_class=ORJSONResponse)

    app.include_router(router)

    app.add_middleware(
        middleware_class=CORSMiddleware,  # type: ignore
        allow_origins=settings.cors.allowed_origins,
        allow_credentials=settings.cors.allow_credentials,
        allow_methods=settings.cors.allowed_methods,
        allow_headers=settings.cors.allowed_headers,
    )

    return app
