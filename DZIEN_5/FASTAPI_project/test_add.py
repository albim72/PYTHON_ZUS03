import requests

url = "http://127.0.0.1:8000/add"
data = {"a":13,"b":89}

response = requests.post(url,json=data)

print(response.json())
