from fastapi import HTTPException, status

import schemas
import models
from database import db_dependency
from hashing import Hash 

def create(payload : schemas.User, db : db_dependency):
    new_user = models.User(
        email = payload.email,
        password = Hash.bcrypt(payload.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, db : db_dependency):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
    return user