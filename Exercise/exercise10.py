import requests
import json
  
URL = "https://httpbin.org/post"
  
mydata = {'address':"Paris"}
  
r = requests.get(url = URL, data = mydata)
print(r.request.headers["Content-Type"])

r = requests.get(url = URL, json = mydata)
print(r.request.headers["Content-Type"])