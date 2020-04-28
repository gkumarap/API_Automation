import requests as REQ


appid = "673c5650a20311041c26d61291b186ae"
id = "2172797"
Base_url = "http://api.openweathermap.org/data/2.5/weather"

params ={"appid":appid,'id':id}

response= REQ.get(Base_url,params=params)

print(response.request.url)
# print(response.text)