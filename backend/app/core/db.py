from motor.motor_asyncio import AsyncIOMotorClient
import certifi
from app.core.config import settings

client = AsyncIOMotorClient(
    settings.MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client[settings.DATABASE_NAME]

