from typing import Optional
from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=3, description="Name of user")
    email: str = Field(..., description="Email of user")
    password: str = Field(..., min_length=4, description="Password of user")


class UserModifyRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: str