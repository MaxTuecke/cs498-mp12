import requests
import time

b = {'k': 'v'}


url_free = 'localhost:5000/img-classification/free'
url_premium = 'localhost:5000/img-classification/premium'
url_config = 'localhost:5000/config'


x = requests.post(url_free, json = myobj)
print(x.text)

time.sleep(3)

x = requests.post(url_config, json = myobj)
print(x.text)

