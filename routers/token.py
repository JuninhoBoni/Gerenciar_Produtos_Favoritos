from services.validate import ValidateGenerateToken
from dependencies import users_db, authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status


router = APIRouter(prefix="/token",
                   tags=['token'],
                   responses={404: {"description": "Not found"}},
                   )


@router.post('/', tags=['token'])
async def login_for_access_token(loc: ValidateGenerateToken = Depends()):
    user = authenticate_user(
        users_db, loc.username, loc.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
