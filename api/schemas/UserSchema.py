from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    pass



class User(UserBase):
    id: int


class UserRead(UserBase):
    id: int
