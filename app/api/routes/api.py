from fastapi import APIRouter

from app.api.routes import authentication, comments, profiles, tags, users
from app.api.routes.announcements import api as announcements

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(profiles.router, tags=["profiles"], prefix="/profiles")
router.include_router(announcements.router, tags=["announcements"])
router.include_router(
    comments.router,
    tags=["comments"],
    prefix="/announcements/{slug}/comments",
)
router.include_router(tags.router, tags=["tags"], prefix="/tags")
