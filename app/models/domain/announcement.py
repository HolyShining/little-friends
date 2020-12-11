from app.models.domain.internal_model import InternalModel
from app.models.domain.users import User

class Announcement(InternalModel):
    user: User
    title: str
    description: str
    start_date: str
    end_date: str
    time: str
    block: bool