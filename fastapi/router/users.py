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
@user_router.get("/{name}")
async def read_user(name : str) :
    found_user = next((user for user in user_list if user.name == name), None)
    if not found_user:
        raise HTTPException(status_code=404, detail="유저를 찾지 못했어요!")
    return {"user": found_user}

#http://localhost:8000/users/
@user_router.post("/")
async def create_user(user : User) -> dict:
    user_list.append(user)
    return {f"{user.name}" :"님 회원가입 완료"}

@user_router.delete("/{name}")
async def delete_user(name: str):
    for idx, user in enumerate(user_list):
        if user.name == name:
            user_list.pop(idx)
            return {"detail": f"{name} 유저 삭제 완료"}
    raise HTTPException(status_code=404, detail="유저를 찾지 못했어요!")

@user_router.put("/{name}")
async def update_user(name: str, new_user: User):
    for idx, user in enumerate(user_list):
        if user.name == name:
            user_list[idx] = new_user
            return {"detail": f"{name} 유저 수정 완료"}
    raise HTTPException(status_code=404, detail="유저를 찾지 못했어요!")