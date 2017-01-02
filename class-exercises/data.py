#import csv and requests for API
import csv
import requests

gen1 = range(1-151)
#Question to answer: What are all types of the Pokemon species in Gen 1?
#Use  data API
#set up URL for API
for x in range(gen1):
endpoint = "http://pokeapi.co/api/v2/"
gen = "pokemon/"+x+"/"
url = endpoint+gen
print(url)
payload = {}

#send request
r = requests.get(url, params=payload)

#organize info from get request and get status
print(r)
pokemon = r.json
print(weather.keys)
