from app.models.schemas.internal_schema import InternalSchema
from app.models.domain.internal_model import InternalModel
from app.models.domain.users import User
from app.models.domain.announcement import Announcement

class Tags(InternalModel):
    announcement: Announcement
    user: User
    content: str
    date: str
