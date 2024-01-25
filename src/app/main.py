from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.router import user, auth

from app.auth.database import Base
from app.auth.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
origin = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(user.router)
app.include_router(auth.router)
