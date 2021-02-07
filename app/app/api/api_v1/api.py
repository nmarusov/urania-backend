from fastapi import APIRouter

from app.api.api_v1.endpoints import auth, tasklist, bpmanager

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(tasklist.router, prefix="/tasklist", tags=["Tasklist"])
api_router.include_router(bpmanager.router, prefix="/bpmanager", tags=["BP Manager"])
