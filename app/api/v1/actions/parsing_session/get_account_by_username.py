from sqlalchemy import func

from app.api.v1.actions.base import ActionBase, ActionError, NotFoundError
from app.api.v1.schemas.parsing_session import ParsingSessionAccountList
from app.models.parsing_session import ParsingSession, ParsingSessionAccount


class GetAccountByUsername(ActionBase):
    class Model(ParsingSessionAccountList):
        pass

    def __call__(self, session_id: int, username: str) -> Model:
        session = self.db.query(ParsingSession).filter(
            ParsingSession.session_id == session_id
        ).first()
        if session is None:
            raise NotFoundError()

        account = self.db.query(ParsingSessionAccount).filter(
            ParsingSessionAccount.session_id == session_id,
            func.lower(ParsingSessionAccount.username) == func.lower(username)
        ).first()

        if account is None:
            raise NotFoundError('Account not found')
        if account.status == ParsingSessionAccount.Status.FAILED:
            raise ActionError('account failed')

        return self.Model.from_orm(account)
