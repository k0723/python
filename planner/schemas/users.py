from typing import List,Optional
from pydantic import BaseModel, constr
from pydantic.networks import EmailStr
from schemas.events import Event

class User(BaseModel):
    email : EmailStr
    password : str
    username : str
    events : Optional[List[Event]]

class UserSignin(BaseModel):
    email : EmailStr
    password : str


