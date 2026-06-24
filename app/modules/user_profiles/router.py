from fastapi import APIRouter, Depends, responses, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.user_profiles.modules import User_profile, User_profile_Json

router = APIRouter(prefix="/user-profiles", tags=["Users"])

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

@router.post('/add/')
def create_user_profile(user_profile: User_profile_Json,
                        db: Session = Depends(get_db)):
    try:
        row = User_profile(
            user_id = user_profile.user_id,
            first_name = user_profile.first_name,
            last_name = user_profile.last_name
        )
        db.add(row)
        db.commit()
    except:
        raise HTTPException(status_code=403, detail="Forbidden")
    return user_profile