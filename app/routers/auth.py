from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import schemas, models,database,utils,aouth2
router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login',response_model=schemas.Token)
def login(user_cridentials : OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(database.get_db)):
    """verifies the user credentials and returns an access token if the credentials are valid

    Args:
        user_cridentials (OAuth2PasswordRequestForm, optional): login details to be varified. Defaults to Depends().
        db (Session, optional): databa session sess. Defaults to Depends(database.get_db).

    Raises:
        HTTPException: when a user entered invalid credentials
        HTTPException: when a user entered invalid credentials

    Returns:
        _type_: schemas.Token
    """
    user = db.query(models.User).filter(models.User.email == user_cridentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify_password(user_cridentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    access_token = aouth2.create_access_token(data={"user_id":user.id})
    return {"access_token": access_token,"token_type":"bearer"}
