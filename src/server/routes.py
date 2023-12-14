from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.middleware import admin_middleware, user_middleware

user_router = APIRouter(prefix="/user", dependencies=[Depends(user_middleware)])
admin_router = APIRouter(prefix="/admin", dependencies=[Depends(admin_middleware)])
base_route = APIRouter(prefix="")  # routes that don't need authentication


@base_route.get("/health", summary="Health check")
async def health_check():
    return JSONResponse(status_code=200, content={"message": "OK"})
