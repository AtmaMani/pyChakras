# main app file

from typing import Optional
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
import json, os
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from mangum import Mangum
import logging


# Create app, just like in Flask
app = FastAPI()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# templates_dir = '/opt/fastapi/templates'
templates_dir = os.path.join(os.environ.get("LAMBDA_RUNTIME_DIR"), "templates")
imgs_dir = "/tmp/imgs"
templates = Jinja2Templates(directory=templates_dir)


@app.get('/hello')
def hello():
    logger.info('Logger /hello was called')
    print('/hello was called')
    return {'Hello': 'World. I am from within the FastAPI within Docker'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id,
            'q': q}


@app.get('/genRandomNumbers/{num_random}')
async def gen_random_ints(num_random: int, upper_limit: Optional[int] = None):
    logger.info('Logger /genRandomNumbers was calleed')
    print('/genRandomNumbers was calleed')
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
    return os.listdir(imgs_dir)

# Upload files
@app.post('/uploadImg')
async def create_upload_img(file: UploadFile = File(...)):
    logger.info("UploadImg is called- within uploadImg")
    print("UploadImg is called- within func")
    if not os.path.exists(imgs_dir):
        os.mkdir(imgs_dir)
        logger.info(f'Made {imgs_dir}')
        print(f'Made {imgs_dir}')
    else:
        logger.info(f'{imgs_dir} exists, reusing it.')
        print(f'{imgs_dir} exists, reusing it.')

    file_list = os.listdir(imgs_dir)
    file_name = f'{len(file_list)+1}.jpg'

    with open(f'{imgs_dir}/{file_name}', 'wb+') as fp:
        fp.write(file.file.read())

    logger.info('Wrote file to disk')
    print('Wrote file to disk')
    return {'Status':'Uploaded',
            'uploaded_files': await list_uploaded_files()}


# Upload files
@app.post('/uploadImg2')
async def create_upload_img2(file: bytes = File(...)):
    print("UploadImg is called- within func2")
    if not os.path.exists(imgs_dir):
        os.mkdir(imgs_dir)
        print(f'Made {imgs_dir}')
    else:
        print(f'{imgs_dir} exists, reusing it.')

    file_list = os.listdir(imgs_dir)
    file_name = f'{len(file_list)+1}.jpg'

    # with open(f'{imgs_dir}/{file_name}', 'wb+') as fp:
    #     # fp.write(file.file.read())
    #     fp.write(file.)

    print('Wrote file to disk')
    # return {'Status':'Uploaded',
    #         'uploaded_files': await list_uploaded_files()}
    return {'Status':'Upload stopped',
            'file_size':len(file)}

# debug - list pwd and ls
@app.get('/getCurrDir')
async def get_current_dir():
    d={}
    d['pwd'] = os.getcwd()
    # d['ls'] = os.listdir()
    d['img_dir_path'] = os.path.abspath(imgs_dir)
    d['img_dir'] = os.listdir(imgs_dir)
    d['templates_dir_path'] = os.path.abspath(templates_dir)
    d['templates_dir'] = os.listdir(templates_dir)

    return d

@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request':request})

handler = Mangum(app)
