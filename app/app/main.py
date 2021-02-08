from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import sentry_sdk

from app.api.api_v1.api import api_router
from app.core.config import settings


sentry_sdk.init(settings.SENTRY_DSN, traces_sample_rate=1.0)

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)
