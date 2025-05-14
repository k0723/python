from fastapi import APIRouter

items_router = APIRouter(prefix="/items")

@items_router.get("/{item_id}")
async def read_item(item_id: int):
    # 임시 데이터, 실제 DB 연동 시 삭제
    return {"item_id": item_id}

# 아이템 생성
@items_router.post("/")
async def create_item(item: dict):
    return {"item": item}

# 아이템 삭제
@items_router.delete("/{item_id}")
async def delete_item(item_id: int):
    # 예제에서는 리스트 또는 DB에서 찾는 로직 필요
    # 여기선 그냥 성공 메시지로 대체
    # 실제 구현 시 삭제 로직 추가하세요
    return {"detail": f"Item {item_id} 삭제 완료"}

# 아이템 업데이트 (전체 or 부분 가능)
@items_router.put("/{item_id}")
async def update_item(item_id: int, item: dict):
    # 업데이트 로직 (DB 또는 리스트 수정)
    return {"detail": f"Item {item_id} 수정 완료", "updated_data": item}