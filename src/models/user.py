import datetime
from pydantic import BaseModel
from pydantic_mongo import ObjectIdField


class User(BaseModel):
    id: ObjectIdField
    """Идентификатор пользователя внутри Telegram"""
    telegram_id: int
    first_name: str
    middle_name: str | None
    last_name: str | None
    phone_number: int | None
    country: str | None
    """Дата начала водительского стажа"""
    driving_experience_at: datetime.date | None
    """Номер водительского удостоверения"""
    drivers_license_number: int | None
    """Дата начала действия водительского удостоверения"""
    vl_date_at: datetime.date | None
    """Дата окончания действия водительского удостоверения"""
    vl_date_to: datetime.date | None
