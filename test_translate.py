import requests

url = "http://127.0.0.1:5000/translate"
data = {"text": "ମୁଁ ଏକ ଭଲ କାମ ଖୋଜୁଛି" }
     
response = requests.post(url, json=data)
print(response.json())
