import requests

baseurl = 'http://restapi.demoqa.com/utilities/weather/city'
def getRequests(url):
    return requests.get(url)
