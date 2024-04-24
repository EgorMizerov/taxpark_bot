from aiogram.client.session import aiohttp


class YandexAPI:
    create_driver_profile_url = 'https://fleet-api.taxi.yandex.net/v2/parks/contractors/driver-profile'

    def __init__(self, client_id: str, api_key:str):
        self.client_id = client_id
        self.api_key = api_key

    async def headers(self):
        return {"X-Client-ID": self.client_id,
                "X-API-Key": self.api_key,
                "Accept-Language": 'ru'}

    async def create_driver_profile(self):
        data = {
            'profile': {
                'hire_date'
            }
        }
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(self.create_driver_profile_url):
                    pass
            except Exception as e:
                print(e)
