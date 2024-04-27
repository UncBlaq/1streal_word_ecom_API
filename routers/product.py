from typing import List

from fastapi import APIRouter, status, Depends

import schemas, oauth2
from database import db_dependency
from services import product as prod

router = APIRouter(
    prefix= "/products",
    tags=["Products"]
)


@router.get("/", status_code= status.HTTP_200_OK, response_model= List[schemas.Product])
def products(db :db_dependency, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return prod.get_all(db)
    # products = db.query(models.Product).all()
    # return products

@router.post("/", status_code= status.HTTP_201_CREATED)
def products(payload: schemas.Product, db : db_dependency, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return prod.create(payload, db)
    # new_product = models.Product(
    #     name = payload.name,
    #     price = payload.price,
    #     qauntity_available = payload.qauntity_available,
    #     owner_id = 1
    # )
    # db.add(new_product)
    # db.commit()
    # db.refresh(new_product)
    # return new_product



@router.get("/{id}", status_code= status.HTTP_200_OK, response_model= schemas.Product)
def product(id: int, db :db_dependency, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return prod.show(id, db)

    # product = db.query(models.Product).filter(models.Product.id == id).first()
    # if not product:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Product with id {id} not found")
    # return product

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def product(id: int, db : db_dependency, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return prod.delete(id, db)
    # product = db.query(models.Product).filter(models.Product.id == id).first()
    # if not product:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Product with id {id} not found")
    # db.delete(product)
    # db.commit()
    # return "product deleted successfully"



@router.put("/{id}", status_code=status.HTTP_200_OK )
def product(id: int, payload: schemas.Product, db : db_dependency, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return prod.update(id, payload, db)


    # product = db.query(models.Product).filter(models.Product.id == id).first()
    
    # if not product:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Product with id {id} not found")
    
    # product.name= payload.name
    # product.price = payload.price
    # product.qauntity_available = payload.qauntity_available  
    
    # db.commit()
    # db.refresh(product)
    # return "Product Updated successfully"

