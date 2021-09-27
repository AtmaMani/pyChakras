# main app file

from typing import Optional
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
import json, os
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from mangum import Mangum

# Create app, just like in Flask
app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/hello')
def hello():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id,
            'q': q}


@app.get('/genRandomNumbers/{num_random}')
async def gen_random_ints(num_random: int, upper_limit: Optional[int] = None):
    from random import randint
    if not upper_limit:
        upper_limit = num_random + 20

    unique_random_list = set()
    if num_random > upper_limit:
        num_random = upper_limit
    while len(unique_random_list) < num_random:
        unique_random_list.add(randint(0, upper_limit))

    return json.dumps(list(unique_random_list))


# Pydantic types for complex JSON Post operations
class Item(BaseModel):
    name: str
    description: Optional[str] = "What an amazing item"
    price: Optional[float] = 10.0
    tax: Optional[float] = price/10


item_list = []
@app.post('/items')
async def create_item(item: Item):
    item.tax = item.price / 10
    item_list.append(item)
    return item


@app.get('/items')
async def get_items():
    return item_list


@app.get('/listFiles')
async def list_uploaded_files():
    return os.listdir('./imgs')

# Upload files
@app.post('/uploadImg')
async def create_upload_img(file: UploadFile = File(...)):
    if not os.path.exists('./imgs'):
        os.mkdir('./imgs')

    file_list = os.listdir('./imgs')
    file_name = f'{len(file_list)+1}.jpg'

    with open(f'./imgs/{file_name}', 'wb+') as fp:
        fp.write(file.file.read())

    return {'Status':'Uploaded',
            'uploaded_files': await list_uploaded_files()}


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})

handler = Mangum(app)