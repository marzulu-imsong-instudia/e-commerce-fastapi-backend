from fastapi import APIRouter, Depends, responses
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.user_profiles.modules import User_profile

router = APIRouter(prefix="/user-profile", tags=["Users"])

@router.get('/')
def get_user_profiles(db: Session = Depends(get_db)):
    query = select(User_profile)
    
    res = db.scalars(query).all()
    
    list_row = []
    
    for row in res:
        list_row.append(
            {
                "id": row.id,
                "user id": row.user_id,
                "first name": row.first_name,
                "last name": row.last_name
            }
        )
        
    return responses.JSONResponse(content=list_row)

@router.get('/{profile_id}')
def get_user_profile_by_id(profile_id:int, db: Session = Depends(get_db)):
    
    row = db.get(User_profile, profile_id)
    
    row_d = {
                "id": row.id,
                "user id": row.user_id,
                "first name": row.first_name,
                "last name": row.last_name
            }
    
    return responses.JSONResponse(content=row_d)