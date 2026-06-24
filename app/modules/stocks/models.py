from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel
from app.core.database import Base

class Stock(Base):
    __tablename__ = "stocks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    color_variant: Mapped[Optional[str]]
    size_variant: Mapped[Optional[str]]
    quantity: Mapped[int]

class Stock_Json(BaseModel):
    
    color_variant: str
    size_variant: str
    quantity: int