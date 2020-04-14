import  requests
import json
#url
url = "https://reqres.in/api/users"

#payload

payload ={'name':'one','job':'member'}

#json format


# json_input = json.loads(payload)


#post request

# response = requests.post(url,json_input)
response = requests.post(url, payload)
print(response)