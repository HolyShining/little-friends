from starlette.requests import Request
from starlette.responses import HTMLResponse
from app.core.config import TEMPLATES
from fastapi import APIRouter
from fastapi.applications import FastAPI

from app.controllers.profile import router as profile_router

router = FastAPI()
# router.include_router(profile_router, prefix="/profile")

@router.get("/")
async def home(request: Request):
    return TEMPLATES.TemplateResponse("index.html", {"request": request})

@router.get("/profile")
async def profile(request: Request):
    return TEMPLATES.TemplateResponse("profile.html", {"request": request})

@router.get("/profile/edit")
async def profile(request: Request):
    return TEMPLATES.TemplateResponse("edit_userinfo.html", {"request": request})

@router.get("/announcements")
async def announcements(request: Request):
    return TEMPLATES.TemplateResponse("announcement/my_announcements.html", {"request": request})

@router.get("/messages")
async def messages(request: Request):
    return TEMPLATES.TemplateResponse("left_menu/message.html", {"request": request})

@router.get("/messages/{id_}")
async def messages(request: Request, id_: str):
    return TEMPLATES.TemplateResponse("show_message.html", {"request": request})

@router.get("/about")
async def about(request: Request):
    return TEMPLATES.TemplateResponse("left_menu/about.html", {"request": request})

@router.get("/contact")
async def about(request: Request):
    return TEMPLATES.TemplateResponse("left_menu/contact.html", {"request": request})

@router.get("/announcements/{id_}")
async def about(request: Request, id_: str):
    return TEMPLATES.TemplateResponse("announcement/details.html", {"request": request})

@router.get("/announcements/{id_}/edit")
async def about(request: Request, id_: str):
    return TEMPLATES.TemplateResponse("announcement/edit.html", {"request": request})

@router.get("/announcement/create")
async def about(request: Request):
    return TEMPLATES.TemplateResponse("announcement/create.html", {"request": request})

@router.get("/pet/new")
async def about(request: Request):
    return TEMPLATES.TemplateResponse("pet/new_pet.html", {"request": request})

@router.get("/pets/{id_}")
async def about(request: Request, id_: str):
    return TEMPLATES.TemplateResponse("pet/pet_info.html", {"request": request})
