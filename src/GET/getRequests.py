import requests


#URI

url = "https://reqres.in/api/users?page=2"

#Request

response = requests.get(url)

#assert response code
print("****")

assert response.status_code == 200;

#get headers
print("*******")
print(response.headers)

#Fetch cookies
print("*************")
print(response.cookies)

#Fetch encoding
print("**********************")

print(response.encoding)

print("**************************************")
print(response.elapsed)

