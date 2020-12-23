from typing import Optional

from app.models.common import DateTimeModelMixin, IDModelMixin
from app.models.domain.internal_model import InternalModel
from app.services import security


class User(InternalModel):
    name: str
    date_of_birth: str
    phone_number: str
    email: str
    address: str
    pet_owner: bool
    # admin: bool
    # block: bool
    # photo: Optional[str] = None


class UserInDB(IDModelMixin, DateTimeModelMixin, User):
    salt: str = ""
    hashed_password: str = ""

    def check_password(self, password: str) -> bool:
        return security.verify_password(self.salt + password, self.hashed_password)

    def change_password(self, password: str) -> None:
        self.salt = security.generate_salt()
        self.hashed_password = security.get_password_hash(self.salt + password)
