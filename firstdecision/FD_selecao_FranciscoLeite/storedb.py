import pandas as pd
from pymongo import MongoClient


username = "root"
password = "root"
host = "localhost"
port = 27017
auth_db = "admin"


connection_string = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}"

prod = pd.read_json("products.json")

prod_lipstick = prod[prod["category"] == "lipstick"]


client = MongoClient(connection_string)
db = client['firstmd']           
collection = db['tb_produto']

prod_dict = prod.to_dict("records")


result = collection.insert_many(prod_dict)