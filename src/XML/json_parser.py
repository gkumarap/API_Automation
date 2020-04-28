import json

#json file
persons = '{"name": "Bob", "languages": ["Python", "Java"]}'

#load python string as json object

person_dict = json.loads(persons)

#print a value from the loaded json

print(person_dict['languages']) #prints list

