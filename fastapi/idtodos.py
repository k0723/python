from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

# 기존 todo_list 를 import 한다고 가정
from todo import todo_list  # 또는 실제 위치에 따라 경로 수정

# 응답 DTO
class IdItem(BaseModel):
    iditem: str

class IdItemList(BaseModel):
    iditems: List[IdItem]

# 라우터 생성
idtodo_router = APIRouter(prefix="/idtodos", tags=["ID+Item 목록"])

@idtodo_router.get("/", response_model=IdItemList)
async def get_iditems():
    result = [{"iditem": f"{todo.id} {todo.item}"} for todo in todo_list]
    return {"iditems": result}
