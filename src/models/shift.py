import datetime
from enum import Enum

from pydantic_mongo import ObjectIdField


class ShiftStatus(Enum):
    Started = 'started'
    Closed = 'closed'


class DriversShift:
    id: ObjectIdField
    user_id: int
    status: ShiftStatus
    cash_amount: int
    cashless_amount: int

    created_at: datetime.datetime
    ended_at: datetime.datetime
