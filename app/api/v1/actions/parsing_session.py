from typing import List

from fastapi import BackgroundTasks

from app.api.v1.actions.base import ActionBase
from app.api.v1.schemas.parsing_session import ParsingSessionCreate, ParsingSessionList
from app.models.parsing_session import ParsingSession, ParsingSessionAccount
from app.services.twitter import twitter_client


class Create(ActionBase):
    class Model(ParsingSessionList):
        pass

    def __call__(self, session: ParsingSessionCreate, background_tasks: BackgroundTasks) -> Model:
        obj = ParsingSession()
        self.db.add(obj)
        self.db.commit()
        clear_usernames = [account.lstrip('https://twitter.com/').lower() for account in session.accounts]
        background_tasks.add_task(self.save_twitter_user_by_usernames, obj.session_id, clear_usernames)
        return self.Model.from_orm(obj)


    async def save_twitter_user_by_usernames(self, parsing_session_id: int, usernames: List[str]):
        twitter_users = await twitter_client.get_users_by_usernames(usernames)
        for username in usernames:
            obj = ParsingSessionAccount(session_id=parsing_session_id, username=username)
            if username in twitter_users:
                obj.status = ParsingSessionAccount.Status.SUCCESS.value
                obj.name = twitter_users[username].name
                obj.twitter_id = twitter_users[username].twitter_id
                obj.followers_count = twitter_users[username].followers_count
                obj.following_count = twitter_users[username].following_count
                obj.description = twitter_users[username].description
            else:
                obj.status = ParsingSessionAccount.Status.FAILED.value
            self.db.add(obj)

        self.db.commit()
            



