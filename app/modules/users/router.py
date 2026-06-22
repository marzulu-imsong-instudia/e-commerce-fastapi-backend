from fastapi import APIRouter, Depends, HTTPException, status, responses
from sqlalchemy.orm import Session
from app.core.database import get_db
from sqlalchemy import select
from app.modules.users.models import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get('/')
def get_users(db: Session = Depends(get_db)):
    query = select(User)
    res = db.scalars(query).all()
    
    # 3. Construct your clean response list
    list_row = []
    for row in res:
        list_row.append({
            "id": row.id, 
            "email": row.email
        })

    # 4. Return standard JSONResponse
    return responses.JSONResponse(content={"users": list_row})

@router.get('/{user_id}')
def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
    
    row_obj = db.get(User, user_id)
    
    row = {
        "id": row_obj.id,
        "email": row_obj.email
    }
    
    return responses.JSONResponse(content=row)
# @router.post("/", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
# def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
#     existing_user = service.get_user_by_email(db, payload.email)
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return service.register_new_user(db, payload)