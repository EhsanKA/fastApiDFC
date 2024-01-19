from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: str

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item