from typing import List


class Address:
    address: str
    lat: float
    lon: float

class OrderType:
    id: str
    name: str


class Order:
    id: str
    short_id: str
    status: str
    type: OrderType
    route_points: List[Address]
    provider: str
    price: str
    payment_method: str
    address_from: Address
    amenities: List[str]
    booked_at: str