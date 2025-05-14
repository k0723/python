from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel,constr

class Todo(BaseModel):
    id : int
    item: constr(strip_whitespace=True, min_length=1)

todo_router = APIRouter(prefix="/todos")

#할 일 정보를 저장할 리스트 => DB 연동으로 변경
todo_list = []

#할 일 조회
#http://localhost:8000/todos
@todo_router.get("/{todo_id}")
async def retrives_todo(todo_id : int):
    return {"todo" : todo_list}
#할 일 상세 조회
#http://localhost:8000/todos/{todo_id}
@todo_router.get("/todos/{todo_id}")
async def get_todo_id_todo(todo_id : int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(status_code=404, detail="할 일 없음 or 찾을 수 없음")

#할 일 생성 
#POST http://localhost:8000/todos/
@todo_router.post("/")
async def add_todo(todo : Todo) -> dict:
    todo_list.append(todo)
    return {"todo" : "할 일을 추가했습니다."}

#할 일 제거
@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    global todo_list
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(idx)
            return {"detail": f"Todo {todo_id} 삭제 완료"}
    raise HTTPException(status_code=404, detail="삭제 실패")

#할 일 업데이트
@todo_router.put("/{todo_id}")
async def update_todo(todo_id: int, updated_todo: Todo):
    global todo_list
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[idx] = updated_todo
            return {"detail": f"Todo {todo_id} 업데이트 완료"}
    raise HTTPException(status_code=404, detail="할 일 없음")