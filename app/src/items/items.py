# items.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/items/")
def read_items():
    return {"items": ["item1", "item2", "item3"]}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
