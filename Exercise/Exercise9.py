import requests
  
URL = "https://httpbin.org/get"
  
r = requests.post(url = URL)

print(r.status_code)