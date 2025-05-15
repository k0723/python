from fastapi import APIRouter

items_router = APIRouter(prefix="/items")

@items_router.get("/{item_id}")
async def read_item(item_id: int):
    item_id : int = Path(..., title = "The ID of the item to get",gt=0, le=10),
    q : str | None = None,
    # 임시 데이터, 실제 DB 연동 시 삭제
    return {"item_id": item_id}

# 아이템 생성
@items_router.post("/")
async def create_item(item: dict):
    return {"item": item}

# 아이템 삭제
@items_router.delete("/{item_id}")
async def delete_item(item_id: int):
    return {"detail": f"Item {item_id} 삭제 완료"}

# 아이템 업데이트 (전체 or 부분 가능)
@items_router.put("/{item_id}")
async def update_item(item_id: int, item: dict):
    # 업데이트 로직 (DB 또는 리스트 수정)
    return {"detail": f"Item {item_id} 수정 완료", "updated_data": item}