import requests


#URI

url ="https://reqres.in/api/users?page=2"

#Request

response=requests.get(url)
print(response.content)