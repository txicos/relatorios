import pandas as pd
from pymongo import MongoClient


username = "root"
password = "root"
host = "localhost"
port = 27017
auth_db = "admin" 


connection_string = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_db}"


client = MongoClient(connection_string)
db = client['firstmd']           
collection = db['tb_produto'] 


documents = collection.find({})


prod_list = list(documents)


prod = pd.DataFrame(prod_list)

# retira mongo _id 
prod = prod.drop('_id', axis=1)

print(prod.head(10))

prod.info()
