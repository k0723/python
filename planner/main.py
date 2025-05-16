from fastapi import FastAPI
from routes import users, events, auth
from database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(events.router)
app.include_router(auth.router)

# 특정 파일을 실행하는 경우 명령어 실행
# 파이썬 내부에 시스템 변수로 import 를 통해서 다른곳에 포함되어 실행될때에는 조건문에 있는 파일이 실행하게 된다

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port = 8000, reload = True)
    