from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.users import User
from app.models.domain.announcement import Announcement
from app.models.domain.internal_model import InternalModel


class Comment(IDModelMixin, DateTimeModelMixin, InternalModel):
    announcement: Announcement
    user: User
    content: str
    date: str
