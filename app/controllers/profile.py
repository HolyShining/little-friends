from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse

from app.api.dependencies.database import get_repository
from app.db.repositories.tags import TagsRepository
from app.models.schemas.tags import TagsInList
from app.core.config import TEMPLATES

router = APIRouter()


# @router.get("", response_class=HTMLResponse)
# async def get_all_tags(request):
#     return TEMPLATES.TemplateResponse("profile.html", {"request": request})
# @router.get("")
# async def get_all_tags(request):
#     return {"hello": 1}
