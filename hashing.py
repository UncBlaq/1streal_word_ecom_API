from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"])

class Hash():
    def bcrypt(password : str):
           hashed_password = pwd_cxt.encrypt(password)
           return hashed_password
    
    def verify(hashed_password, plain_password):
          return pwd_cxt.verify( plain_password, hashed_password)

