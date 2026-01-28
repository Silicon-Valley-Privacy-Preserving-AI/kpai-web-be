from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=3, description="Name of user")
    email: str = Field(..., description="Email of user")
    password: str = Field(..., min_length=4, description="Password of user")



class UserModifyRequest(BaseModel):
    username: str = Field(..., min_length=3, description="Name of user")
    email: str = Field(..., description="Email of user")


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True