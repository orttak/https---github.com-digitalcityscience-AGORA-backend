from typing import Union
from fastapi import FastAPI

from app.auth import config

app = FastAPI()


@app.get("/")
def read_root():
    print(config.settings)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
