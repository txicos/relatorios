import pandas as pd
from pymongo import MongoClient
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import RedirectResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

username = "root"
password = "root"
host = "mongo"
port = 27017
auth_db = "admin" 

connection_string = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}"  

client = MongoClient(connection_string)
db = client['firstmd']           
collection = db['tb_produto'] 

@app.get("/", status_code=status.HTTP_200_OK)
async def docs_redirect():
    return RedirectResponse(url='/docs')


@app.get("/prod", status_code=status.HTTP_200_OK)
def get_products():
  
  try:

    documents = collection.find({})


    prod_list = list(documents)


    prod = pd.DataFrame(prod_list)
    
    prod['created_at'] = prod['created_at'].astype(str)
    prod['updated_at'] = prod['updated_at'].astype(str)
    prod = prod.fillna(0)    

    # retira mongo _id 
    if "_id" in prod.columns:
      prod = prod.drop('_id', axis=1)

    json_data = prod.to_dict(orient='records')
    return json_data

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e)) 


