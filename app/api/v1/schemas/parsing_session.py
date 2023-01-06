from typing import Set
from pydantic import BaseModel, constr


class ParsingSessionCreate(BaseModel):
    accounts: Set[constr(regex="^https://twitter\.com/[a-zA-Z0-9_]{1,15}")]


class ParsingSessionList(BaseModel):
    session_id: int

    class Config:
        orm_mode = True


class ParsingSessionAccountStatusList(BaseModel):
    username: str
    status: str

    class Config:
        orm_mode = True


class ParsingSessionAccountList(BaseModel):
    twitter_id: str
    username: str
    name: str
    followers_count: int
    following_count: int
    description: str

    class Config:
        orm_mode = True


class ParsingSessionAccountTweetsList(BaseModel):
    tweet_id: str
    text: str

    class Config:
        orm_mode = True
