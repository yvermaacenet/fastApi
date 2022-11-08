from fastapi import Depends, HTTPException , status
from fastapi.security import OAuth2PasswordBearer
# from JWTtoken import verify_token
from JWTtoken import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login_auth")

def get_current_user(token_data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token_data , credentials_exception)