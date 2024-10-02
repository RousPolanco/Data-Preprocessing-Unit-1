import json
 
def import_json (filename):
    with open (filename, 'r') as file:
        data = json.load (file)
    return data

product_data = import_json ('products.json')
print (product_data)