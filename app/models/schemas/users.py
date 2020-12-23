from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl

from app.models.domain.users import User
from app.models.schemas.internal_schema import InternalSchema


class UserInLogin(InternalSchema):
    email: EmailStr
    password: str


class UserInCreate(UserInLogin):
    name: str
    date_of_birth: str
    phone_number: str
    address: str
    pet_owner: bool


class UserInUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    bio: Optional[str] = None
    image: Optional[HttpUrl] = None


class UserWithToken(User):
    token: str


class UserInResponse(InternalSchema):
    user: UserWithToken
