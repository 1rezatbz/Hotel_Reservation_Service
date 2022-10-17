from fastapi import HTTPException
from jose import (jwt, JWTError)
from src.crud import get_user
from password import verify_password
from src import (rediss, crud, schemas)


SECRET_KEY = "c674646851df8654cb92ffa2ac6647d66526453e7b0f88e197ae09bc467e5779"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(user_id: int):
    encoding = {"user_id": str(user_id)}
    encoded_jwt = jwt.encode(encoding, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decoded_access_token(db, token):
    credentials_exeption = HTTPException(status_code=401, detail="could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exeption
        token_data = schemas.TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exeption
    if rediss.get_token(user_id):
        user = crud.get_user_by_id(db, user_id=token_data.user_id)
        if user is None:
            raise credentials_exeption
    return user

