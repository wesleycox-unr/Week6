import json


people = {
            "people": [
                {"Name":"Jane Smith",
                "Age": 23,
                "Address": "123 Fake St"},
                {"Name":"Slim Dusty",
                "Age":44}
            ]
            
}

#print(people)

with open("people_json.txt","w") as outfile:
    json.dump(people, outfile, indent=4)