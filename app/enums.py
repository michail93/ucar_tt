from enum import Enum


class StatusEnum(Enum):
    WAITING = "waiting"
    IN_WORK = "in_work"
    CLOSED = "closed"


class SourceEnum(Enum):
    OPERATOR = "operator"
    MONITORING = "monitoring"
    PARTNER = "partner"
