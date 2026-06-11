from app.core.db import db
from datetime import datetime
from bson import ObjectId

class FactRepository:

    @staticmethod
    async def create_fact(fact_data):

        # pyrefly: ignore [deprecated]
        fact_data["created_at"] = datetime.utcnow()

        result = await db.facts.insert_one(fact_data)

        return str(result.inserted_id)

    @staticmethod
    async def get_all_facts():

        facts = await db.facts.find().to_list(length=100)

        for fact in facts:
            fact["_id"] = str(fact["_id"])

        return facts


    @staticmethod
    async def get_fact_by_id(fact_id):

        fact = await db.facts.find_one(
            {"_id": ObjectId(fact_id)}
        )
        if fact:
            fact["_id"] = str(fact["_id"])
        return fact

    @staticmethod
    async def delete_fact(fact_id):

        result = await db.facts.delete_one(
            {"_id": ObjectId(fact_id)}
        )

        return result.deleted_count

    @staticmethod
    async def update_fact(
        fact_id,
        updated_content
    ):

        result = await db.facts.update_one(
            {"_id": ObjectId(fact_id)},
            {
                "$set": {
                    "content": updated_content
                }
            }
        )

        return result.modified_count