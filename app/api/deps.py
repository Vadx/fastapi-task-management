from typing import Generator
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.config import settings
from app.core.security import verify_token
from app.crud.user import user
from app.models.user import User
from app.schemas.token import TokenData

security = HTTPBearer()

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(security)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = verify_token(token.credentials)
        if payload is None:
            raise credentials_exception
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except (jwt.JWTError, ValidationError):
        raise credentials_exception
    
    current_user = user.get_by_username(db, username=token_data.username)
    if current_user is None:
        raise credentials_exception
    return current_user

def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
