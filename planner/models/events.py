from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database.connection import Base
from sqlmodel import SQLModel,Field
from typing import List, Optional

class Event(Base, SQLModel, table = True):
    __tablename__ = "events"

    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str


    # 🔗 외래키 설정: 소유 유저 ID
    user_id:int = Column(Integer, ForeignKey("users.id"))

    # 🔁 관계 설정: Event → User
    owner:int = relationship("User", back_populates="events")

class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description : Optional[str]
    tags : List[str]
    location : Optional[str]