from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
import models
from database import db_dependency
from hashing import Hash
import jwttoken

router = APIRouter(
     tags = ["Authentification"]
)

@router.post('/login')
def login(
      db: db_dependency,
    payload: OAuth2PasswordRequestForm = Depends()
           ):
    user = db.query(models.User).filter(models.User.email == payload.username).first()
    if user is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(user.password, payload.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    #generate jwt token and return
    

   
    access_token = jwttoken.create_access_token(
        data={"sub": user.email}
    )
    return {
        "access_token" : access_token, 
        "token_type" : "bearer"
        }