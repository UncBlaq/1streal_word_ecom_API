from fastapi import FastAPI

from database import engine
import models

import routers.product, routers.user, routers.authentification



app = FastAPI(
   
)


#whenever a model is found, Add to the database
models.Base.metadata.create_all(bind = engine)

app.include_router(routers.authentification.router)
app.include_router(routers.product.router)
app.include_router(routers.user.router)


# @app.post("/products", status_code= status.HTTP_201_CREATED,tags=["PRODUCT"])
# def products(payload: schemas.Product, db : db_dependency):
#     new_product = models.Product(
#         name = payload.name,
#         price = payload.price,
#         qauntity_available = payload.qauntity_available,
#         owner_id = 1
#     )
#     db.add(new_product)
#     db.commit()
#     db.refresh(new_product)
#     return new_product


# @app.get("/products", status_code= status.HTTP_200_OK, response_model= List[schemas.Product],  tags=["PRODUCT"])
# def products(db :db_dependency):
#     products = db.query(models.Product).all()
#     return products


# @app.get("/products/{id}", status_code= status.HTTP_200_OK, response_model= schemas.Product, tags=["PRODUCT"])
# def product(id, db :db_dependency):
#     product = db.query(models.Product).filter(models.Product.id == id).first()
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Product with id {id} not found")
#     return product

# @app.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT , tags=["PRODUCT"])
# def product(id, db : db_dependency):
#     product = db.query(models.Product).filter(models.Product.id == id).first()
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Product with id {id} not found")
#     db.delete(product)
#     db.commit()
#     return "product deleted successfully"



# @app.put("/products/{id}", status_code=status.HTTP_200_OK , tags=["PRODUCT"])
# def product(id, payload: schemas.Product, db : db_dependency):
#     product = db.query(models.Product).filter(models.Product.id == id).first()
    
#     if not product:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Product with id {id} not found")
    
#     product.name= payload.name
#     product.price = payload.price
#     product.qauntity_available = payload.qauntity_available  
    
#     db.commit()
#     db.refresh(product)
#     return "Product Updated successfully"





# @app.post("/user", response_model=schemas.ShowUser, tags= ["USER"])
# def user(payload : schemas.User, db : db_dependency):
 
#     new_user = models.User(
#         email = payload.email,
#         password = Hash.bcrypt(payload.password)
#     )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# @app.get("/user/{id}", response_model=schemas.ShowUser, tags= ["USER"])
# def user(id, db : db_dependency):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")
#     return user
    


    
    