from typing import List
from pydantic import BaseModel, constr

class Event(BaseModel):
    id : int,
    title : str,
    image : str,
    description : str,
    tags : List[str],
    location : str