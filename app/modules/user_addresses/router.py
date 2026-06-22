from fastapi import APIRouter, Depends, responses
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.user_addresses.modules import User_address

router = APIRouter(prefix="/user-addresses", tags=["Users"])

@router.get('/')
def get_user_addresses(db: Session = Depends(get_db)):
    query = select(User_address)
    
    res = db.scalars(query).all()
    
    list_row = []
    
    for row in res:
        list_row.append(
            {
                "id": row.id,
                "user id": row.user_id,
                "state": row.state,
                "district": row.district,
                "zipcode": row.zipcode
            }
        )
        
    return responses.JSONResponse(content=list_row)

@router.get('/{profile_id}')
def get_user_profile_by_id(profile_id:int, db: Session = Depends(get_db)):
    
    row = db.get(User_address, profile_id)
    
    row_d = {
                "id": row.id,
                "user id": row.user_id,
                "state": row.state,
                "district": row.district,
                "zipcode": row.zipcode
            }
    
    return responses.JSONResponse(content=row_d)