from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def read_root():
    with open('flower-api.json') as json_file:
        data = json.load(json_file)
    return data

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

