from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from . import schemas
from fastapi import Depends, status , HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= 'login')


#we want 3 variables for a jwt token,
# secret key for signature, algorithm for header and data for payload, also expiry time 
# so that it does not happen like user is logged in forever

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes 

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm= ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str , credentials_exception):
    
    try:
        payload = jwt.decode(token, SECRET_KEY , algorithms=[ALGORITHM])
        print("JWT PAYLOAD:", payload)
        id: str = payload.get("user_id")
        print("USER ID FROM TOKEN:", id)

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)

    except JWTError as e:
        print("JWT ERROR:", e)
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credentials could not be verified",
        headers={"WWW-Authenticate":"Bearer"}
    ) 
    
    return verify_access_token(token, credentials_exception)