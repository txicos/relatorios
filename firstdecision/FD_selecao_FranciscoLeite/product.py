import pandas as pd
import re
import matplotlib.pyplot as plt

def format_datetime(input_string):
  match = re.match(r"(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):\d+\.\d+([+-]\d{2}:\d{2})", input_string)
  if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    hour = match.group(4)
    minute = match.group(5)


    return f"{day}/{month}/{year} {hour}:{minute}"
  else:
    return "Invalid date format"

def buscar_produto(df, produto):
  searched = prod[prod["category"] == produto]
  return searched

prod = pd.read_json("products.json")

prod_lipstick = prod[prod["category"] == "lipstick"]

print(prod["category"].unique())

prod_pencil = buscar_produto(prod,"pencil")

prod_pencil['created_at']=prod_pencil['created_at'].astype(str).apply(format_datetime)

prod_pencil.to_json('pencil.json')

count_pencil = prod_pencil.groupby(['brand'])['brand'].count()



count_pencil_top_10 = count_pencil.to_frame().nlargest(10, 'brand')

plt.figure()

count_pencil_top_10.plot(kind='bar')

plt.savefig("pencil_brand_counts.png", dpi=300, transparent=True)

#plt.show()



