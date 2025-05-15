from fastapi import APIRouter, HTTPException, Path, Query
from pydantic import BaseModel, constr
from typing import List, Optional
from model import Todo,TodoItem,TodoItems

class TodoUpdate(BaseModel):
    item: constr(strip_whitespace=True, min_length=1)

todo_router = APIRouter(prefix="/todos", tags=["할 일"])

todo_list: List[Todo] = [
    Todo(id=1, item="1st todo"),
    Todo(id=2, item="2nd todo")
]

# 1. 전체 목록 (전체 항목만)
@todo_router.get("/", response_model=TodoItems)
async def get_all_todos() -> dict:
    result = [{"id": todo.id, "item": todo.item} for todo in todo_list]
    return {"item": result}

# 1-1. 전체 목록 (List[TodoItem] 직접 반환)
@todo_router.get("/all", response_model=List[TodoItem])
async def get_all_todos_all_atr():
    return [{"id": todo.id, "item": todo.item} for todo in todo_list]

# 2. 상세 조회
@todo_router.get("/{todo_id}")
async def get_todo(todo_id: int = Path(..., ge=1, le=1000)):
    for todo in todo_list:
        if todo.id == todo_id:
            return todo
    if not result:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")

# 3. 검색
@todo_router.get("/search")
async def search_todos(item: Optional[str] = Query(None)):
    if item:
        result = [todo for todo in todo_list if item in todo.item]
        return result
    return todo_list

# 4. 추가
@todo_router.post("/", status_code=201)
async def add_todo(todo: Todo):
    if any(existing.id == todo.id for existing in todo_list):
        raise HTTPException(status_code=400, detail="중복된 ID입니다.")
    todo_list.append(todo)
    return {"message": "할 일을 추가했습니다."}

# 5. 수정
from pydantic import BaseModel

class TodoUpdate(BaseModel):
    item: constr(strip_whitespace=True, min_length=1)

@todo_router.put("/{todo_id}")
async def update_todo(todo_id: int, updated: TodoUpdate):
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list[idx].item = updated.item
            return {"message": "할 일을 수정했습니다."}
    raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")

# 6. 삭제
@todo_router.delete("/{todo_id}",status_code=204)
async def delete_todo(todo_id: int):
    for idx, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(idx)
            return {"message": "할 일을 삭제했습니다."}
    raise HTTPException(status_code=404, detail="할 일을 찾을 수 없습니다.")
