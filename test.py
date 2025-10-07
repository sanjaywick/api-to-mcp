import requests

payload = {"body": {"id": 456, "name": "Fluffy", "tag": "cat"}}
resp = requests.post("http://127.0.0.1:8000/invoke/addPet", json=payload)
print(resp.json())
