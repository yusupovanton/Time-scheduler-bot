from handlers.imports import *
from handlers.config import BOT_OWNER


class IsOwnerFilter(BoundFilter):
    """
    Custom filter "is_owner".
    """
    key = "is_owner"

    def __init__(self, is_owner):
        self.is_owner = is_owner

    async def check(self, message: types.Message):
        print(message.from_user.id)
        return message.from_user.id == BOT_OWNER

