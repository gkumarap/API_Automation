# importing the requests library
import requests

# api-endpoint
URL = "http://maps.googleapis.com/maps/api/geocode/json"

#location
location = "Anna university chennai"


#giving param dict(OBJECT) for the parameters to be sent to api

PARAMS = {'address':location}

#get request

response = requests.get(url= URL, params= PARAMS )
print(response.text)

#extract data in json format

json_format = response.json()

