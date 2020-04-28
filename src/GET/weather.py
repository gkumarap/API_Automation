from src.common.GET import getRequests
from src.common.GET import baseurl
import json
import jsonpath



url = baseurl+'/chennai'
print(url)
response = getRequests(url)
print(response.text)
json_response = json.loads(response.text)
City = jsonpath.jsonpath(json_response,'City')
print(json_response['Temperature'], response.request.url)
print(json_response['Humidity'],response.request.headers)
print(json_response['WeatherDescription'],response.request.path_url)
print(json_response['WindSpeed'],response.request.body)
print(json_response['WindDirectionDegree'])



# assert
# print(json_response)
