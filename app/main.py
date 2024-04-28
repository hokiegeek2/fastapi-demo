from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str

items = {}

@app.get("/")
async def root():
    return {"message": "Hello from hokiegeek2"}

@app.get("/item/")
async def get_items() -> list:
    return items.items()

@app.get("/item/{item_id}")
async def get_item(item_id: int) -> dict:
    return {"item_id": item_id}

@app.post("/item/")
async def createitem(item_id: int, item_name) -> dict:
    items[item_name] = Item(id=item_id,name=item_name)
    return {"message": f"item {items[item_name]} created"}
