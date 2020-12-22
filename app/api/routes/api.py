from fastapi import APIRouter

from app.api.routes import authentication, comments, tags, users

router = APIRouter()
router.include_router(authentication.router, tags=["authentication"], prefix="/users")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(
    comments.router,
    tags=["comments"],
    prefix="/announcements/{slug}/comments",
)
router.include_router(tags.router, tags=["tags"], prefix="/tags")
