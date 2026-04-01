from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field
from typing import Optional, List

from models.database import Base

# ================= SQLAlchemy Models =================
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    logs = relationship("LogDB", back_populates="owner")

class LogDB(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mood = Column(Integer)
    sleep = Column(Float)
    work_hours = Column(Float)
    screen_time = Column(Float)
    journal_text = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    
    owner = relationship("UserDB", back_populates="logs")

# ================= Pydantic Models =================

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class Log(BaseModel):
    mood: int = Field(..., ge=1, le=5)
    sleep: float = Field(..., ge=0)
    work_hours: float = Field(..., ge=0)
    screen_time: float = Field(..., ge=0)
    journal_text: Optional[str] = None

class LogResponse(BaseModel):
    status: str
    burnout_score: int
    insight: str
    suggestions: List[str]
    quote: str
    all_quotes: List[str]
    music: List[str]
    alerts: List[str]
