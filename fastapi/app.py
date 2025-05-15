from fastapi import FastAPI, Path
import todo
from router import users,items
from middleware.CORSmiddleware import CORSmiddleware

app = FastAPI()
# FastAPI (웹) 인스턴스를 생성
app.add_middleware(CORSmiddleware)
app.include_router(todo.todo_router)
app.include_router(users.user_router)
app.include_router(items.items_router)

@app.get("/")
async def welcome() -> dict:
    return {"message": "HelloWorld"}
