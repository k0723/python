from fastapi import APIRouter, HTTPException, Depends,Response
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta

from database.connection import SessionLocal
from models.users import User as UserModel
from schemas.users import User, UserSignin
from middleware.auth import get_current_user
from auth.jwt_handler import create_access_token,create_refresh_token;

router = APIRouter(prefix="/users", tags=["users"])

# 비밀번호 해싱 도구
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 회원가입
@router.post("/signup")
def signup(user: User, db: Session = Depends(get_db)):
    existing = db.query(UserModel).filter(UserModel.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")
    
    hashed_pw = pwd_context.hash(user.password)
    new_user = UserModel(
        email=user.email,
        username=user.username,
        hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "회원가입 완료", "user_id": new_user.id}

# 로그인
@router.post("/login")
def login(response : Response, user : UserSignin, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 틀렸습니다.")
    # 로그인 성공 시 JWT 토큰 생성
    access_token = create_access_token(data={"sub" : db_user.email}, expires_delta = timedelta(minutes=15))
    refresh_token = create_refresh_token(data={"sub" : db_user.email})

    response.set_cookie(key = "refresh_token", value = refresh_token, httponly = True)

    return {
        "access_token" : access_token,
        "token_type" : "bearer",
        "message": "로그인 성공"}

