import json

def load_products(file='products_list.json'):
    with open(file,'r') as f:
        data = json.load(f)
    return data