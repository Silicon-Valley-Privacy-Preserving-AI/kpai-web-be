from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, description="Name of user")
    email: str = Field(..., description="Email of user")
    password: str = Field(..., min_length=4, description="Password of user")


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True