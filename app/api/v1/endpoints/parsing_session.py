from typing import List

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.api.v1.actions import parsing_session
from app.api.v1.schemas.parsing_session import ParsingSessionCreate
from app.db import get_db

router = APIRouter(
    prefix='',
    tags=['users']
)


@router.post('/users/', response_model=parsing_session.Create.Model)
async def create(
        session: ParsingSessionCreate,
        background_tasks: BackgroundTasks,
        db: Session = Depends(get_db),
):
    return parsing_session.Create(db)(session, background_tasks)


@router.get('/users/status', response_model=List[parsing_session.GetAccountsStatus.Model])
async def create(
        session_id: int,
        db: Session = Depends(get_db),
):
    return parsing_session.GetAccountsStatus(db)(session_id)


@router.get('/users/{username}', response_model=parsing_session.GetAccountByUsername.Model)
async def create(
        session_id: int,
        username: str,
        db: Session = Depends(get_db),
):
    return parsing_session.GetAccountByUsername(db)(session_id, username)


@router.get('/tweets/{twitter_id}', response_model=List[parsing_session.GetTweets.Model])
async def create(
        session_id: int,
        twitter_id: str,
        db: Session = Depends(get_db),
):
    return parsing_session.GetTweets(db)(session_id, twitter_id)
