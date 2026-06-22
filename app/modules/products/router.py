from fastapi import APIRouter, Depends, responses
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.products.models import Product

router = APIRouter(prefix="/products", tags=["Users"])

@router.get('/')
def get_products(db: Session = Depends(get_db)):
    query = select(Product)
    res = db.scalars(query).all()
    
    list_row = []
    for row in res:
        list_row.append({
            "id": row.id,
            "name": row.name,
            "price": row.price,
            "stock_id": row.stock_id,
            "date_added": str(row.date_added)
        })
        
    return responses.JSONResponse(content=list_row)

@router.get('/{product_id}')
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    
    row = db.get(Product, product_id)
    
    row_d = {
            "id": row.id,
            "name": row.name,
            "price": row.price,
            "stock_id": row.stock_id,
            "date_added": str(row.date_added)
            }
    
    return responses.JSONResponse(content=row_d)