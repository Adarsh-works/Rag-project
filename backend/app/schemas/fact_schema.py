from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FactCreate(BaseModel):
    user_id: str
    content: str


class FactUpdate(BaseModel):
    content: str


class FactResponse(BaseModel):
    id: str
    user_id: str
    content: str