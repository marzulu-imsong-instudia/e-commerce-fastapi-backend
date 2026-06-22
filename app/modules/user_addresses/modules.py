from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from sqlalchemy import ForeignKey
from pydantic import BaseModel

class User_address(Base):
    __tablename__ = "user_addresses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    state: Mapped[Optional[str]]
    district: Mapped[Optional[str]]
    zipcode: Mapped[Optional[str]]
    
class User_address_Json(BaseModel):
    
    id: int
    user_id: int
    state: str
    district: str
    zipcode: str