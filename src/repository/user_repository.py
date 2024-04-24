from pydantic_mongo import AbstractRepository

from src.models.user import User


class UserRepository(AbstractRepository[User]):
    class Meta:
        collection_name = 'users'
