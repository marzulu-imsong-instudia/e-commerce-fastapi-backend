from fastapi import APIRouter, Depends, responses, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.user_addresses.modules import User_address, User_address_Json

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

@router.get('/{address_id}')
def get_user_address_by_id(address_id:int, db: Session = Depends(get_db)):
    
    row = db.get(User_address, address_id)
    
    row_d = {
                "id": row.id,
                "user id": row.user_id,
                "state": row.state,
                "district": row.district,
                "zipcode": row.zipcode
            }
    
    return responses.JSONResponse(content=row_d)

@router.post('/add/')
def create_user_profile(user_address: User_address_Json,
                        db: Session = Depends(get_db)):
    try:
        row = User_address(
            user_id = user_address.user_id,
            state = user_address.state,
            district = user_address.district,
            zipcode = user_address.zipcode
        )
        db.add(row)
        db.commit()
    except:
        raise HTTPException(status_code=403, detail="Forbidden")
    return user_address