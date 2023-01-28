from fastapi import APIRouter

from .operations import router as operation_router

from . import auth, operations, reports


router = APIRouter()
router.include_router(auth.router)
router.include_router(operation_router)
router.include_router(reports.router)