from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String)
    price = Column(DECIMAL)
    qauntity_available = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="products")



class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True)
    email = Column(String)
    password = Column(String)

    products = relationship("Product", back_populates="owner")


