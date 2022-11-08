from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash ():
    def bcrypt_password(get_password:str):
        return pwd_context.hash(get_password)

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)    