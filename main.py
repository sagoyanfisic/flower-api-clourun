import requests
import json
from fastapi import FastAPI

app = FastAPI()

# @app.get("/renipress/")
# def list_renipress_all():
#     renipress_susalud = "http://www.susalud.gob.pe/consultaIPRESSMapasOra.asp"
#     response = rq.get(renipress_susalud, stream=True)
#     result = json.loads(response.text)
#     data = {"data":result}
#     result data
    
    
@app.post("/data_sat/")
def load_data_sat(placa=None):
    data = {}
    #request_json = request.get_json()
    if not placa:
        data = {
            'message': "Error, no se mando ninguna placa!",
            'status': "success",
            'status_code': 200,
        }
        return data

    url = "https://app2.sat.gob.pe:8443/smartsatrestv2/consultarapida"
    # placa axb126
    querystring = {"codContribuyente":"0","idUser":"1","placa":placa}
    payload = ""
    headers = {
      'Content-Type': "application/json",
      'authorization': "Basic QUtJQUpTNVRTS1hVN1BROlo3cUlTcytHOHVBVkY1SWpEL1lnSnJMdFM1dDVod2JnTw==",
      'cache-control': "no-cache",
      'Postman-Token': "c2c06042-d6dd-43b5-ac96-e5560cd1bbf7"
      }

    # response = None
    # while (response == None):
    #     try:
    #         response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    #         break
    #     except:
    #         print("Connection refused by the server..")
    #         print("Let me sleep for 5 seconds")
    #         print("ZZzzzz...")
    #         time.sleep(5)
    #         print("Was a nice sleep, now let me continue...")
    #         continue

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    if response.status_code != 200 :
        data = {
            'message': "Error!",
            'status': "Fail",
            'status_code': response.status_code,
        }
        return data

    if len(response.text) == 43:
        data = {
            'message': "Error, la placa no existe en la base de datos",
            'status': "success",
            'status_code': response.status_code,
        }
        return data

    data = {
        'message': "Se crearon los datos satisfactoriamente.",
        'status': "success",
        'status_code': response.status_code,
        'data': json.loads(response.text)
    }
    return data

    
    
