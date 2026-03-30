from fastapi import APIRouter

from backend.core.config import settings


from .auth import router as auth_router
from .users import router as users_router


router = APIRouter(
    prefix=settings.api.v1.prefix,
)


router.include_router(users_router)
router.include_router(auth_router)
