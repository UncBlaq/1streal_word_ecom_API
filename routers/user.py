from typing import List

from fastapi import APIRouter,HTTPException, status 
from database import db_dependency
import schemas
import models
from services import user as owner

router = APIRouter(
    prefix="/user",
    tags=["USERS"]
)




@router.post("/", response_model=schemas.ShowUser)
def user(payload : schemas.User, db : db_dependency):
    return owner.create(payload, db)
 
    # new_user = models.User(
    #     email = payload.email,
    #     password = Hash.bcrypt(payload.password)
    # )
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)
    # return new_user


@router.get("/{id}", response_model=schemas.ShowUser)
def user(id, db : db_dependency):
    return owner.show(id, db)
    # user = db.query(models.User).filter(models.User.id == id).first()
    # if user is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    # return user
    