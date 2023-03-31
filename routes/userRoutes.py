from fastapi import APIRouter,status,HTTPException,Depends
from models import userModal
from sqlalchemy.orm import Session
from schemas.userSchema import UserCreate,UserOutput,UserSignin
from hashPassword import hash_password,verify_password
from database import get_db
from auth import create_access_token,get_current_user
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from schemas.tokenSchema import tokenSchema


router= APIRouter(
    prefix= "/users"
)

@router.post("/signup",status_code=status.HTTP_201_CREATED,response_model=UserOutput)
def createUser(user: UserCreate,db: Session= Depends(get_db)):
    try:
        new_user= userModal.User(**user.dict())
        new_user.password= hash_password(new_user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_226_IM_USED,detail=f"{err}")
              

    return new_user

@router.get("/{id}",response_model=UserOutput)
async def getUser(id: int,db: Session= Depends(get_db),get_current_user:int = Depends(get_current_user)):
    user= db.query(userModal.User).filter(userModal.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id: {id},Does not exist")

    return user    

@router.post('/signin',response_model= tokenSchema)
def signIn(userCredential: OAuth2PasswordRequestForm= Depends(),db: Session= Depends(get_db)):
    
    user= db.query(userModal.User).filter(userModal.User.username == userCredential.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid User")
    
    if not verify_password(userCredential.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid User")
    
    access_token= create_access_token({"user_id": user.id})

    return {"access_token": access_token,"token_type": "bearer"}
    
