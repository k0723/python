from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    image = Column(String)
    description = Column(String)
    tags = Column(String)
    location = Column(String)

    # 🔗 외래키 설정: 소유 유저 ID
    user_id = Column(Integer, ForeignKey("users.id"))

    # 🔁 관계 설정: Event → User
    owner = relationship("User", back_populates="events")
