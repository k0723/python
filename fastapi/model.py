from pydantic import BaseModel, constr
from typing import List 

class Todo(BaseModel):
    id: int
    item: constr(strip_whitespace=True, min_length=1)

class TodoItem(BaseModel):
    id: int
    item: str

class TodoItems(BaseModel):
    item: List[TodoItem]