from pydantic import BaseModel, Field
import uuid
from typing import Optional

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    email: str = Field (...)


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
   

