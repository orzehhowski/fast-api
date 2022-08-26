from fastapi import FastAPI
from enum import Enum

app = FastAPI()
# uvicorn [filename]:[FastAPI instance name] [--reload - developer mode] 

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

# optional parameters\
@app.get('/items2/{item_id}')
# http://127.0.0.1:8000/items2/cool_item?q=abc
# http://127.0.0.1:8000/items/foo?short=1
# short can be 1, True, true, on, yes
async def get_items2(item_id: str, q: str or None = None, short: bool = False):
    item = {'id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item     
    
@app.get('/needy-q-params/')
def needy_q_params(needy: str):
    return {'param': needy}
