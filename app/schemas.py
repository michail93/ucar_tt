from datetime import datetime

from pydantic import BaseModel

from .enums import SourceEnum, StatusEnum


class IncidentCreate(BaseModel):
    description: str
    status: StatusEnum
    source: SourceEnum
    creation_date_time: datetime | None = None


class IncidentUpdate(BaseModel):
    status: StatusEnum


class IncidentDB(BaseModel):
    id: int
    description: str
    status: StatusEnum
    source: SourceEnum
    creation_date_time: datetime
