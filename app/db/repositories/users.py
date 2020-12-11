from typing import Optional

from app.db.errors import EntityDoesNotExist
from app.db.queries.queries import queries
from app.db.repositories.base import BaseRepository
from app.models.domain.users import User, UserInDB


class UsersRepository(BaseRepository):
    async def get_user_by_email(self, *, email: str) -> UserInDB:
        user_row = await queries.get_user_by_email(self.connection, email=email)
        if user_row:
            return UserInDB(**user_row)

        raise EntityDoesNotExist("user with email {0} does not exist".format(email))

    async def get_user_by_name(self, *, name: str) -> UserInDB:
        user_row = await queries.get_user_by_name(
            self.connection,
            name=name,
        )
        if user_row:
            return UserInDB(**user_row)

        raise EntityDoesNotExist(
            "user with name {0} does not exist".format(name),
        )

    async def create_user(
        self,
        *,
        name: str,
        email: str,
        password: str,
    ) -> UserInDB:
        user = UserInDB(name=name, email=email)
        user.change_password(password)

        async with self.connection.transaction():
            user_row = await queries.create_new_user(
                self.connection,
                name=user.name,
                email=user.email,
                salt=user.salt,
                hashed_password=user.hashed_password,
            )

        return user.copy(update=dict(user_row))

    async def update_user(  # noqa: WPS211
        self,
        *,
        user: User,
        name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        photo: Optional[str] = None,
    ) -> UserInDB:
        user_in_db = await self.get_user_by_name(name=user.name)

        user_in_db.name = name or user_in_db.name
        user_in_db.email = email or user_in_db.email
        user_in_db.bio = bio or user_in_db.bio
        user_in_db.photo = photo or user_in_db.photo
        if password:
            user_in_db.change_password(password)

        async with self.connection.transaction():
            user_in_db.updated_at = await queries.update_user_by_name(
                self.connection,
                name=user.name,
                new_name=user_in_db.name,
                new_email=user_in_db.email,
                new_salt=user_in_db.salt,
                new_password=user_in_db.hashed_password,
                new_bio=user_in_db.bio,
                new_photo=user_in_db.photo,
            )

        return user_in_db
