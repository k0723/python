from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from models.events import Event as EventModel
from schemas.events import Event
from typing import List
import json

router = APIRouter(prefix="/events", tags=["events"])

# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 이벤트 생성
@router.post("/", response_model=Event)
def create_event(event: Event, db: Session = Depends(get_db)):
    new_event = EventModel(
        title=event.title,
        image=event.image,
        description=event.description,
        tags=json.dumps(event.tags),  # 리스트 → 문자열로 저장
        location=event.location
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return Event(
        id=new_event.id,
        title=new_event.title,
        image=new_event.image,
        description=new_event.description,
        tags=event.tags,
        location=new_event.location
    )

# 전체 이벤트 조회
@router.get("/", response_model=List[Event])
def get_all_events(db: Session = Depends(get_db)):
    events = db.query(EventModel).all()
    return [
        Event(
            id=ev.id,
            title=ev.title,
            image=ev.image,
            description=ev.description,
            tags=json.loads(ev.tags),  # 문자열 → 리스트로 변환
            location=ev.location
        ) for ev in events
    ]

# 단일 이벤트 조회
@router.get("/{event_id}", response_model=Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="이벤트를 찾을 수 없습니다.")
    return Event(
        id=event.id,
        title=event.title,
        image=event.image,
        description=event.description,
        tags=json.loads(event.tags),
        location=event.location
    )

# 이벤트 삭제
@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(EventModel).filter(EventModel.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="이벤트가 존재하지 않습니다.")
    db.delete(event)
    db.commit()
    return {"message": f"{event_id}번 이벤트가 삭제되었습니다."}