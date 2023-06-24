from ..database import get_db
from .. import models,schemas,utils
from fastapi import  FastAPI, HTTPException, Response, status, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import exc


router = APIRouter(
    prefix="/users",
    tags=["user authentication"],
) 
    
    
@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        hashed_password = utils.hash_password(user.password)
        user.password = hashed_password
        created_user = models.User(**user.dict())
        db.add(created_user)
        db.commit()
        db.refresh(created_user) 
        return created_user 
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with email {user.email} already exists")
    except exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
@router.get("/{user_id}", response_model=schemas.UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    
    return user