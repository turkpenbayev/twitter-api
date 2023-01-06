from sqlalchemy import Column, DateTime, Integer, func


class CreateTimeTrackableMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


class UpdateTimeTrackableMixin:
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), server_onupdate=func.now(), nullable=False)


class CreateUpdateTimeTrackableMixin(CreateTimeTrackableMixin, UpdateTimeTrackableMixin):
    pass


class CreatedByTrackableMixin:
    created_by_id = Column(Integer, index=True, nullable=False)
