from typing import Optional
from pydantic import BaseModel, constr
from models.Event import Event

class User(BaseModel):
    email : EmailStr
    password : str
    username : str
    events : Optional[List[Event]] = None

class userSignin(BaseModel):
    email : EmailStr
    password : str

