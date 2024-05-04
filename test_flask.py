import requests
import time

b = {'k': 'v'}


url_free = 'http://54.160.65.50:5000/img-classification/free'
url_premium = 'http://54.160.65.50:5000/img-classification/premium'
url_config = 'http://54.160.65.50:5000/config'


x = requests.post(url_free, json = b)
print(x.text)

time.sleep(3)

x = requests.get(url_config)
print(x.text)

