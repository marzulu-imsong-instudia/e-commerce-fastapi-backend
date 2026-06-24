from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, func, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]]
    price: Mapped[int]
    stock_id: Mapped[int] = mapped_column(ForeignKey("stocks.id", ondelete="CASCADE"))
    date_added: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=False),
        server_default=func.now()
    )
    
class Product_Json(BaseModel):
    

    name: str
    price: int
    stock_id: int
    date_added: datetime