import requests
  
URL = "https://httpbin.org/get"
  
r = requests.get(url = URL)

print(r.status_code)