from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from pydantic import BaseModel
from app.core.database import Base

class User_profile(Base):
    __tablename__ = "user_profiles"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    first_name: Mapped[Optional[str]]
    last_name: Mapped[Optional[str]]
    
class User_profile_Json(BaseModel):
    
    user_id: int
    first_name: str
    last_name: str