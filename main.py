from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get('/')
async def root():
    return {'mess': 'hello'}


# order is important - items/basic must be b4 items/<var>, so basic wont be readen as this var
# so the first one path is always more important
@app.get('/items/basic')
def get_basic_item():
    return {'item': 'basic item'}


# parameters in decorator and function must have the same names
@app.get("/items/{id}")
# id is automatically parsed to int, and this is simple data validation
def get_item(id: int):
    return {'item id': id}


class ModelName(str, Enum):
    # thats machine learning models
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/models/{model_name}')
# eg. /models/resnet
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
def read_file(file_path:str):
    return {'file_path': file_path}


fake_db = [{'id': x} for x in range(10)]

@app.get('/items/')
# http://127.0.0.1:8000/items/?start=4&limit=7
def get_items(start: int = 0, limit: int = 10):
    return fake_db[start : limit]
