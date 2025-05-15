from fastapi import APIRouter, Request, HTTPException, Depends
from auth.jwt_handler import create_access_token
from jose import jwt, JWTError

from middleware.auth import get_current_user

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/refresh")
def refresh_token(request: Request):
    refresh_token = request.cookies.get("refresh_token")
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh token missing")
    
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token(data={"sub": email})
    return {"access_token": new_access_token, "token_type": "bearer"}


@router.get("/me")
def get_me(current_user : str = Depends(get_current_user)):
    return {email: current_user}