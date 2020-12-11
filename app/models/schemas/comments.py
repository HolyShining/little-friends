from typing import List

from app.models.domain.comments import Comment
from app.models.schemas.internal_schema import InternalSchema


class ListOfCommentsInResponse(InternalSchema):
    comments: List[Comment]


class CommentInResponse(InternalSchema):
    comment: Comment


class CommentInCreate(InternalSchema):
    content: str
