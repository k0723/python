from fastapi import FastAPI
from routes import users, events, auth
from database.connection import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(events.router)
app.include_router(auth.router)