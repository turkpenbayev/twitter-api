from datetime import datetime, timezone, timedelta
from pydantic import BaseModel


class QuestionCreate(BaseModel):
    content: str

    class Config:
        orm_mode = True