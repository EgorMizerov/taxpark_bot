from typing import List, Any


class Address:
    def __init__(self, address: str, lat: float, lon: float):
        self.address = address
        self.lat = lat
        self.lon = lon


class OrderType:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class Event:
    def __init__(self, event_at: str, order_status: str):
        self.event_at = event_at
        self.order_status = order_status


class DriverProfile:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class License:
    def __init__(self, number: str):
        self.number = number


class Car:
    def __init__(self, id: str, brand_model: str, license: License, callsign: str):
        self.id = id
        self.brand_model = brand_model
        self.license = license
        self.callsign = callsign


class DriverWorkRule:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class Order:
    def __init__(self,
                 id: str,
                 short_id: int,
                 status: str,
                 created_at: str,
                 booked_at: str,
                 provider: str,
                 category: str,
                 address_from: Address,
                 route_points: List[Address],
                 events: List[Event],
                 ended_at: str,
                 payment_method: str,
                 driver_profile: DriverProfile,
                 car: Car,
                 type: OrderType,
                 price: str,
                 amenities: List[str],
                 cancellation_description: str,
                 order_time_interval: Any
                 ):
        self.id = id
        self.short_id = short_id
        self.status = status
        self.created_at = created_at
        self.booked_at = booked_at
        self.provider = provider
        self.category = category
        self.address_from = address_from
        self.route_points = route_points
        self.events = events
        self.ended_at = ended_at
        self.payment_method = payment_method
        self.driver_profile = driver_profile
        self.car = car
        self.type = type
        self.price = price
        self.amenities = amenities
        self.cancellation_description = cancellation_description
        self.order_time_interval = order_time_interval
