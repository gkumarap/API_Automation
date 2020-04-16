from common.GET import getRequests


url = "http://restapi.demoqa.com/utilities/weather/city/chennai"

response = getRequests(url)
print(response.text)
