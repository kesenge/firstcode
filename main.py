from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 定义数据模型
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# 模拟数据库
db = []

# 1. 增 (Create)
@app.post("/items/")
def create_item(item: Item):
    db.append(item)
    return item

# 2. 查 (Read - 获取所有)
@app.get("/items/", response_model=List[Item])
def read_items():
    return db

# 3. 改 (Update)
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(db):
        if item.id == item_id:
            db[i] = updated_item
            return {"message": "更新成功"}
    raise HTTPException(status_code=404, detail="未找到该项目")

# 4. 删 (Delete)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i, item in enumerate(db):
        if item.id == item_id:
            del db[i]
            return {"message": "删除成功"}
    raise HTTPException(status_code=404, detail="未找到该项目")