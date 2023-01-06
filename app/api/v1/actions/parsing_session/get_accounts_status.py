from typing import List

from app.api.v1.actions.base import ActionBase, NotFoundError
from app.api.v1.schemas.parsing_session import ParsingSessionAccountStatusList
from app.models.parsing_session import ParsingSession, ParsingSessionAccount


class GetAccountsStatus(ActionBase):
    class Model(ParsingSessionAccountStatusList):
        pass

    def __call__(self, session_id: int) -> List[Model]:
        session = self.db.query(ParsingSession).filter(
            ParsingSession.session_id == session_id
        ).first()
        if session is None:
            raise NotFoundError()

        accounts_status = self.db.query(ParsingSessionAccount).filter(
            ParsingSessionAccount.session_id == session_id
        ).all()
        return [self.Model.from_orm(obj) for obj in accounts_status]
