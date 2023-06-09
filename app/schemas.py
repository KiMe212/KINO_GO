from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    age: int


class SignUp(BaseModel):
    email: str
    password: str
