from fastapi import APIRouter, Depends, responses, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.products.models import Product,Product_Json

router = APIRouter(prefix="/products", tags=["Users"])

@router.get('/')
def get_products(db: Session = Depends(get_db)):
    query = select(Product)
    
    res = db.scalars(query).all()
    # res = select_all(Product)
    
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
    # row = select_one(Product, product_id)
    
    row_d = {
            "id": row.id,
            "name": row.name,
            "price": row.price,
            "stock_id": row.stock_id,
            "date_added": str(row.date_added)
            }
    
    return responses.JSONResponse(content=row_d)

@router.post('/add/')
def create_user_profile(product: Product_Json,
                        db: Session = Depends(get_db)):
    try:
        row = Product(
            name = product.name,
            price = product.price,
            stock_id = product.stock_id,
            date_added = product.date_added
        )
        db.add(row)
        db.commit()
    except:
        raise HTTPException(detail=403, detail="Forbidden")
    return product

# Separation of concerns
# Handlers -> Routes | JSON parse | Serialize | validate | Pass to Services | Send as response
# Services -> Caching | SMS Service | Pass to Repository | Return to Handlers
# Repository -> Db Interactions | Return to service
