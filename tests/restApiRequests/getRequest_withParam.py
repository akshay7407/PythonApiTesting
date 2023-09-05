import requests

param = {"name":"akshay","email":"akshayTesingWorl@gmail.com"}
response = requests.get("https://httpbin.org/get",params=param)
print(response.text)