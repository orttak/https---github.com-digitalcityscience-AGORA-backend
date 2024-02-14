from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from typing import Optional, List
from sqlalchemy.orm import Session
from app.models import user_model
from app.auth.database import get_db
from app.auth import utils
from app.schemas import user_login

router = APIRouter(prefix="/users", tags=["users"])


# @router.post(
#     "/", status_code=status.HTTP_201_CREATED, response_model=user_login.UserOut
# )
# def create_user(user: user_login.UserCreate, db: Session = Depends(get_db)):
#     try:
#         # hash the password = user.password
#         hashed_password = utils.hash(user.password)
#         user.password = hashed_password
#         new_user = user_model.User(**user.model_dump())
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return new_user
#     except Exception as error:
#         raise HTTPException(
#             status_code=500, detail=f"Error while creating user {error.__cause__}"
#         )


# @router.get("/{id}", response_model=user_login.UserOut)
# def get_user(
#     id: int, db: Session = Depends(get_db),
# ):
#     user = db.query(user_model.User).filter(user_model.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail="user not found")
#     return user
