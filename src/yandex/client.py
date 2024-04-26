import datetime

from aiogram.client.session import aiohttp

from src.models.user import User


class YandexAPI:
    create_driver_profile_url = 'https://fleet-api.taxi.yandex.net/v2/parks/contractors/driver-profile'

    def __init__(self, client_id: str, api_key: str, park_id: str):
        self.client_id = client_id
        self.api_key = api_key
        self.park_id = park_id

    def _headers(self):
        return {
            "X-Client-ID": self.client_id,
            "X-API-Key": self.api_key,
            "X-Park-ID": self.park_id,
            # TODO: генерировать при запросе
            "X-Idempotency-Token": "sagausghasuigashiughaioshguiahgaweg",
            "Accept-Language": 'ru',
        }

    async def create_driver_profile(self, user: User) -> None:
        now = datetime.date.today()
        data = {
            'account': {
                'balance_limit': '0',
                'work_rule_id': '8f0ae1a24d3a413b91d118ed702b4ff5'
            },
            'order_provider': {
                'partner': True,
                'platform': True,
            },
            'person': {
                'contact_info': {
                    'phone': user.phone_number,
                },
                'driver_license': {
                    'country': user.driver_license.country,
                    'expiry_date': user.driver_license.expiry_date,
                    'issue_date': user.driver_license.issue_date,
                    'number': user.driver_license.number,
                },
                'driver_license_experience': {
                    'total_since_date': user.driver_license.driver_license_experience,
                },
                'full_name': {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'middle_name': user.middle_name,
                }
            },
            'profile': {
                'hire_date': f'{now.year}-{now.month}-{now.day}'
            }
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(url=self.create_driver_profile_url, json=data, headers=self._headers()) as response:
                    print(response.status)
                    return None
            except Exception as e:
                print(e)
