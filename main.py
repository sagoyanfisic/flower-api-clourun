from fastapi import FastAPI
import json

app = FastAPI()


#flower list
@app.get("/list/flowers/")
async def list_flower_all():
    with open('flower-api.json') as json_file:
        data = json.load(json_file)
    return data

#flower detail
@app.get("/detail/flower/{item_id}")
async def detail_flower(item_id: str):
    with open('flower-api.json') as json_file:
        data = json.load(json_file)
        flower = {}
        for item in data['flower_data']:
            if item['id'] == int(item_id):
                flower.update({
                    'id':item['id'],
                    'name':item['name'],
                    'scientific_name':item['scientific_name'],
                    'description':item['description'],
                    'applications':item['applications'],
                    'properties':item['properties'],
                })
    return json.load(flower)

#flower detail
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

