from jose import JWTError, jwt
from datetime import datetime,timedelta
from . import schemas,database,models
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_access_token(token : str,cridential_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get("user_id")
        if id is None:
            raise cridential_exception
        token_data =schemas.TokenData(id=id)
    except JWTError:
        raise cridential_exception
    return token_data
    
def get_current_user(token : str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
    cridential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token,cridential_exception)
    user =db.query(models.User).filter(models.User.id == token.id).first()
    return user