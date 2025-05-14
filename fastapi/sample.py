from fastapi import FastAPI
from router import users,items
from router import todo

app = FastAPI()

app.include_router(users.user_router)
app.include_router(items.items_router)
app.include_router(todo.todo_router)

@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

