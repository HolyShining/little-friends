from app.models.domain.internal_model import InternalModel


class InternalSchema(InternalModel):
    class Config(InternalModel.Config):
        orm_mode = True
