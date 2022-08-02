import requests

responce = requests.get("http://127.0.0.1:3000/api/cars/1")   # use GET request - .....requests.get(......
print(responce.json())