from datetime import datetime
from typing import Optional

from pypika import Parameter as CommonParameter, Query, Table


class Parameter(CommonParameter):
    def __init__(self, count: int) -> None:
        super().__init__("${0}".format(count))


class TypedTable(Table):
    __table__ = ""

    def __init__(
        self,
        name: Optional[str] = None,
        schema: Optional[str] = None,
        alias: Optional[str] = None,
        query_cls: Optional[Query] = None,
    ) -> None:
        if name is None:
            if self.__table__:
                name = self.__table__
            else:
                name = self.__class__.__name__

        super().__init__(name, schema, alias, query_cls)


class Users(TypedTable):
    __table__ = "users"

    id: int
    name: str
    date_of_birth: datetime
    phone_number: str
    email: str
    address: str
    pet_owner: bool
    admin: bool
    block: bool


class Announcement(TypedTable):
    __table__ = "announcement"

    id: int
    user_id: int
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    created_at: datetime
    updated_at: datetime


class Tags(TypedTable):
    __table__ = "tags"

    id: int
    name: str
    user_id: int


class TagsForAnnouncement(TypedTable):
    __table__ = "tags_for_announcement"

    announcement_id: int
    tag_id: int


class Comments(TypedTable):
    __table__ = "comments"

    id: int
    announcement_id: int
    user_id: int
    content: str


class Pets(TypedTable):
    __table__ = "pets"

    id: int
    name: str
    user_id: int
    date_of_birth: datetime
    breed: str
    preferences: str


class PetsForAnnouncement(TypedTable):
    __table__ = "pets_for_announcement"

    announcement_id: int
    pet_id: int


users = Users()
announcement = Announcement()
tags = Tags()
tags_for_announcement = TagsForAnnouncement()
comments = Comments()
pets = Pets()
pets_for_announcement = PetsForAnnouncement()
