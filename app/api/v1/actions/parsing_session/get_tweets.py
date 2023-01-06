from typing import List

from app.api.v1.actions.base import ActionBase, ActionError, NotFoundError
from app.api.v1.schemas.parsing_session import ParsingSessionAccountTweetsList
from app.models.parsing_session import ParsingSession, ParsingSessionAccount
from app.models.tweet import Tweet


class GetTweets(ActionBase):
    class Model(ParsingSessionAccountTweetsList):
        pass

    def __call__(self, session_id: int, twitter_id: str) -> List[Model]:
        session = self.db.query(ParsingSession).filter(
            ParsingSession.session_id == session_id
        ).first()
        if session is None:
            raise NotFoundError('Session not found')

        account = self.db.query(ParsingSessionAccount).filter(
            ParsingSessionAccount.session_id == session_id,
            ParsingSessionAccount.twitter_id == twitter_id
        ).first()

        if account is None:
            raise NotFoundError('Account not found')
        if account.status == ParsingSessionAccount.Status.FAILED:
            raise ActionError('Account failed')

        tweets = self.db.query(Tweet).filter(
            Tweet.parsing_session_account_id == account.id
        ).all()

        return [self.Model.from_orm(obj) for obj in tweets]
