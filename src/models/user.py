import datetime
from typing import Optional

from pydantic import BaseModel, constr
from pydantic_mongo import ObjectIdField


class DriverLicense(BaseModel):
    """Водительские удостоверения"""

    """Серия и номер водительского удостоверения"""
    number: constr(min_length=10, max_length=10)
    """Дата начала водительского стажа"""
    driver_license_experience: constr(pattern=r'^\d{4}-\d{2}-\d{2}$')
    """Дата выдачи водительского удостоверения в формате ISO 8601 без временной зоны"""
    issue_date: constr(pattern=r'^\d{4}-\d{2}-\d{2}$')
    """Дата окончания действия водительского удостоверения в формате ISO 8601 без временной зоны"""
    expiry_date: constr(pattern=r'^\d{4}-\d{2}-\d{2}$')
    """Страна выдачи водительского удостоверения (Трехбуквенный код)"""
    country: str


class User(BaseModel):
    id: ObjectIdField
    key: str
    referal_key: int
    telegram_id: int
    first_name: str
    middle_name: str
    last_name: str
    phone_number: constr(pattern=r'(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}')

    driver_license: DriverLicense

    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None
