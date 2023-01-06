from enum import Enum

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.common import CreateTimeTrackableMixin


class ParsingSession(CreateTimeTrackableMixin, Base):
    session_id = Column(Integer, primary_key=True, nullable=False)

    accounts = relationship('ParsingSessionAccount', back_populates='session')


class ParsingSessionAccount(Base):
    class Status(str, Enum):
        SUCCESS = 'success'
        PENDING = 'pending'
        FAILED = 'failed'

    id = Column(Integer, primary_key=True, nullable=False)
    session_id = Column(Integer, ForeignKey(
        'twitter_api_parsingsession.session_id', ondelete='CASCADE'), index=True, nullable=False)
    session = relationship('ParsingSession', back_populates='accounts')
    username = Column(String(256), nullable=False)
    twitter_id = Column(String(56), nullable=True, index=True)
    name = Column(String(256), nullable=True)
    description = Column(String, nullable=True)
    following_count = Column(Integer, nullable=True)
    followers_count = Column(Integer, nullable=True)
    status = Column(String(16), nullable=False, index=True, server_default="{%s}"%(Status.PENDING.value))
