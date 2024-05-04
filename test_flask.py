import requests
import time

b = {'k': 'v'}


url_free = '54.160.65.50:5000/img-classification/free'
url_premium = '54.160.65.50:5000/img-classification/premium'
url_config = '54.160.65.50:5000/config'


x = requests.post(url_free, json = myobj)
print(x.text)

time.sleep(3)

x = requests.post(url_config, json = myobj)
print(x.text)

