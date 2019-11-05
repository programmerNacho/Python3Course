import requests
import os

params = {"q": "pizza"}
r = requests.get("http://www.bing.com/search", params=params)

# HTTP Status Code: https://www.tutorialspoint.com/http/http_status_codes.htm
print("Status:", r.status_code)

f = open(os.path.abspath("./page.html"), "w+")
f.write(r.text)