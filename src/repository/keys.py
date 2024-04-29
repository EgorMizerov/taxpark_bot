import string
import random

from src.repository.user_repository import UserRepository


async def check_key_uniqueness(user_repository: UserRepository, key: str) -> bool:
    key = await user_repository.find_one_by({'key': key})
    if key is None:
        return True
    else:
        return False


async def generate_unique_key() -> str:
    while True:
        all_chars = string.ascii_letters + string.digits + "_-+=()№@#?/\\"
        new_key = ''.join(random.choice(all_chars) for _ in range(9))
        if check_key_uniqueness(new_key):
            return new_key
