from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base import Base
from app.models.common import CreateTimeTrackableMixin


class Tweet(CreateTimeTrackableMixin, Base):
    id = Column(Integer, primary_key=True, nullable=False)
    parsing_session_account_id = Column(Integer, ForeignKey(
        'twitter_api_parsingsessionaccount.id', ondelete='CASCADE'), index=True, nullable=False)
    tweet_id = Column(String(56), nullable=False)
    text = Column(String, nullable=False)
