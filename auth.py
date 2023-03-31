from jose import jwt,JWTError
from datetime import datetime,timedelta
from schemas.tokenSchema import tokenDataSchema
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from envVariables import envObj



oauth2_scheme= OAuth2PasswordBearer(tokenUrl='users/signin')


def create_access_token(data:dict):
    to_encode= data.copy()

    expire= datetime.utcnow() + timedelta(minutes=envObj.EXPIRATION_TIME)
    to_encode.update({"exp": expire})

    token= jwt.encode(to_encode,envObj.SECRET_KEY,algorithm=envObj.ALGORITHM)

    return token

def verify_access_token(token:str,credential_exception):

    try:
        payload= jwt.decode(token,envObj.SECRET_KEY,algorithms=envObj.ALGORITHM)

        id= payload.get("user_id")

        if id is None:
            raise credential_exception
        
        token_data= tokenDataSchema(id= id)
        
    except JWTError:
        raise credential_exception
    
    return token_data
    

def get_current_user(token:str =Depends(oauth2_scheme),db: Session= Depends(get_db)):

    credential_exception= HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token not valid",headers={"WWW-Authenticate": "Bearer"})

    return verify_access_token(token,credential_exception)
    



    



