from fastapi import APIRouter,Query
from typing import Optional, List

items_router = APIRouter(prefix="/items")

@items_router.get("/{item_id}")
async def read_item(
    item_id: int,  # <- 누락되어 있었던 item_id 추가
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        description="검색할 아이템 이름"
    ),
    limit: int = Query(
        10,
        gt=0,
        le=100,
        title="결과 개수 제한"
    ),
    tags: List[str] = Query(
        default=["default"],
        alias="item-tags",
        description="아이템 태그 목록 (예: ?item-tags=a&item-tags=b)"
    ),
):
    return {
        "item_id": item_id,
        "query": q,
        "limit": limit,
        "tags": tags
    }

# 아이템 생성
@items_router.post("/")
async def create_item(item: dict):
    return {"item": item}

# 아이템 삭제
@items_router.delete("/{item_id}")
async def delete_item(item_id: int):
    return {"detail": f"Item {item_id} 삭제 완료"}

# 아이템 업데이트
@items_router.put("/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"detail": f"Item {item_id} 수정 완료", "updated_data": item}