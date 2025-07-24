from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# @app.get("/items")
# async def items():
#     return {"items"}

# @app.get("/items/{id}")
# async def get_item(id):
#     return {"id": id}

# OPtional parameter
# @app.get("/item/{id}")
# async def get_item(id: int, a: str | None = None):
#     if a:
#         return{"item_id":id, "name":a}
#     else:
#         return{"item_id":id}
    
    
class Item(BaseModel):
        id : int
        name : str
        dept : str

db: List[Item] = []

@app.post("/details")
async def post_items(item:Item):
    db.append(item)
    return item

@app.get("/details/{item_id}")
async def get_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
        
        
@app.get("/hello")
async def show():
    return {"hello"}