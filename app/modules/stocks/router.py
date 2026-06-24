from fastapi import APIRouter, Depends, responses, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.stocks.models import Stock, Stock_Json

router = APIRouter(prefix="/stocks", tags=["Users"])

@router.get('/')
def get_stocks(db: Session = Depends(get_db)):
    query = select(Stock)
    res = db.scalars(query).all()
    
    list_row = []
    for row in res:
        list_row.append({
            "id": row.id,
            "color variant": row.color_variant,
            "size variant": row.size_variant,
            "quantity": row.quantity
        })
        
    return responses.JSONResponse(content=list_row)

@router.get('/{stock_id}')
def get_stock_by_id(stock_id: int, db: Session = Depends(get_db)):
    
    row = db.get(Stock, stock_id)
    
    row_d = {
            "id": row.id,
            "color variant": row.color_variant,
            "size variant": row.size_variant,
            "quantity": row.quantity
            }
    
    return responses.JSONResponse(content=row_d)

@router.post('/add/')
def create_user_profile(stock: Stock_Json,
                        db: Session = Depends(get_db)):
    try:
        row = Stock(
            color_variant = stock.color_variant,
            size_variant = stock.size_variant,
            quantity = stock.quantity
        )
        db.add(row)
        db.commit()
    except:
        raise HTTPException(detail=403, detail="Forbidden")
    return stock