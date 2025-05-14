from fastapi import APIRouter

items_router = APIRouter(prefix="/items")

#http://localhost:8000/users/1234
@items_router.get("/{items_id}")
async def read_items(items_id : int):
    return {"user_id" : user_id}

#http://localhost:8000/users/
@items_router.post("/")
async def create_items(items : dict):
    return {"user" : items}