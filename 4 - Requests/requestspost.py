import requests
import os

my_data = {"name": "Nacho", "email": "ignacio.example@example.co"}
r = requests.post("http://www.w3schools.com/php/welcome.php", data=my_data)

f = open(os.path.abspath("myfile.html"), "w+")
f.write(r.text)