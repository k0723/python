from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlmodel import SQLModel
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL,  connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind= engine)
Base = declarative_base()
#테이블 샏성
def conn():
    SQLModel.metadata.create_all(engine)


