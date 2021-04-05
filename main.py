from fastapi import FastAPI
import json
import requests as rq

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
    return flower

#flower detail
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/renipress/")
def list_renipress_all():
    renipress_susalud = "http://www.susalud.gob.pe/consultaIPRESSMapasOra.asp"
    try:
        response = rq.get(renipress_susalud, stream=True)
        return response.json()["result"]
    except rq.HTTPError:
        return


@app.get("/renipress/{renipress_id}")
def list_renipress_id(renipress_id: int):
    renipress_susalud = "http://www.susalud.gob.pe/consultaIPRESSMapasOra.asp"
    try:
        args = {"resource_id": renipress_id}
        response = rq.get(renipress_susalud, params=args, stream=True)
        return response.json()["result"]
    except rq.HTTPError:
        return
