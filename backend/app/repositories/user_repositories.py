from app.core.db import db

class UserRepository:

    @staticmethod
    async def create_user(user_data):
        result = await db.users.insert_one(user_data)
        return str(result.inserted_id)

    @staticmethod
    async def get_all_users():
        users = await db.users.find().to_list(length=100)
        return users