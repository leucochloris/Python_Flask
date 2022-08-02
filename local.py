import requests

# responce = requests.get("http://127.0.0.1:3000/api/cars/0")   # use GET request - for receive the data (by the index)
# responce = requests.delete("http://127.0.0.1:3000/api/cars/2")  # use DELETE request - for delete data (by the index)

# responce = requests.post("http://127.0.0.1:3000/api/cars/5", {"name": "Lada", "count_in_stock": '1'})  # use POST request - for append data (by the index)........
# responce = requests.post("http://127.0.0.1:3000/api/cars/6", {"name": "Mazerati", "count_in_stock": '3'})  # use POST request - for append data (by the index)

responce = requests.put("http://127.0.0.1:3000/api/cars/5", {"name": "Lada", "count_in_stock": 111})  # use PUT request - for change data (by the index)      ********Unlike the POST, we refer to existing indexes, ONLY we are change value
responce = requests.put("http://127.0.0.1:3000/api/cars/6", {"name": "Mazerati", "count_in_stock": 321})  # use PUT request - for change data (by the index)  ********Unlike the POST, we refer to existing indexes ONLY we are change value

'''
We do not use a database, so - every time (depends to method) the data will not be saved
'''


print(responce.json())
