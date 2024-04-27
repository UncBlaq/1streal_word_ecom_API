from fastapi import HTTPException, status

from database import db_dependency
import models
import schemas

def get_all(db: db_dependency):
    products = db.query(models.Product).all()
    return products

def create(payload : schemas.Product, db:db_dependency):
    new_product = models.Product(
        name = payload.name,
        price = payload.price,
        qauntity_available = payload.qauntity_available,
        owner_id = 1
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def delete(id: int, db : db_dependency):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with id {id} not found")
    db.delete(product)
    db.commit()
    return "product deleted successfully"

def update(id : int, payload : schemas.Product, db : db_dependency):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with id {id} not found")
    
    product.name= payload.name
    product.price = payload.price
    product.qauntity_available = payload.qauntity_available  
    
    db.commit()
    db.refresh(product)
    return "Product Updated successfully"


def show(id : int, db: db_dependency):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Product with id {id} not found")
    return product
