from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel,constr

user_router = APIRouter(prefix="/users")

class User(BaseModel):
    id : str
    pwd : str
    name : str

user_list = []

#http://localhost:8000/users/1234
@user_router.get("/{user_id}")
async def read_user(user_id : int) -> dict:
    return {"user_id" : user_id}

#http://localhost:8000/users/
@user_router.post("/")
async def create_user(user : User) -> dict:
    user_list.append(user)
    return {f"{user.name}" :"님 회원가입 완료"}

# #할 일 상세 조회
# #http://localhost:8000/todos/{todo_id}
# @todo_router.get("/{todo_id}")
# async def get_todo_id_todo(todo_id : int) -> dict:
#     for todo in todo_list:
#         if todo.id == todo_id:
#             return {"todo": todo}
#     raise HTTPException(status_code=404, detail="할 일 없음 or 찾을 수 없음")

# #할 일 제거
# @todo_router.delete("/{todo_id}")
# async def delete_todo(todo_id: int):
#     global todo_list
#     for idx, todo in enumerate(todo_list):
#         if todo.id == todo_id:
#             todo_list.pop(idx)
#             return {"detail": f"Todo {todo_id} 삭제 완료"}
#     raise HTTPException(status_code=404, detail="삭제 실패")

# #할 일 업데이트
# @todo_router.put("/{todo_id}")
# async def update_todo(todo_id: int, updated_todo: Todo):
#     global todo_list
#     for idx, todo in enumerate(todo_list):
#         if todo.id == todo_id:
#             todo_list[idx] = updated_todo
#             return {"detail": f"Todo {todo_id} 업데이트 완료"}
#     raise HTTPException(status_code=404, detail="할 일 없음")