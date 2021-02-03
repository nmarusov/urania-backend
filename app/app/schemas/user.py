from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    login: str
    full_name: Optional[str] = None


# Additional properties to return via API
class User(UserBase):
    pass
