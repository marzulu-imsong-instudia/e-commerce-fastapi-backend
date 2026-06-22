from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[Optional[str]]

class User_Json(BaseModel):
    email: str