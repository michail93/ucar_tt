from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, text
from sqlmodel import Field, SQLModel

from .enums import SourceEnum, StatusEnum


class Incident(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str
    status: StatusEnum
    source: SourceEnum
    creation_date_time: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP")
        )
    )



