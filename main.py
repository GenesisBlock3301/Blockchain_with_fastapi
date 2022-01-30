from fastapi import FastAPI
from model import DataModel
from fastapi.encoders import jsonable_encoder
from deploy_contract import ASSETREGISTER

app = FastAPI()

@app.post("/")
async def setData(data:DataModel):
    ASSETREGISTER.functions.setData(data.id).transact()
    return jsonable_encoder({"message":"Successfully created"})


@app.get("/")
async def getData():
    get_data = ASSETREGISTER.functions.getData().call()
    return get_data