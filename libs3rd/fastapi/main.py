import time
import asyncio
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hello/{name}")
def read_item(name: Optional[str] = "Ted"):
    asyncio.sleep(10)
    return f"Hello {name}"