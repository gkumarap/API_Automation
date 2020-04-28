import json

import requests
import jsonpath

url ="https://reqres.in/api/users?page=2"
#send get request

response= requests.get(url)

#parse response to json format

json_response = json.loads(response.text)

# print(json_response)

#get value from json path

total = jsonpath.jsonpath(json_response,'page')

print(total[0])