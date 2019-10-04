# people dictionary

#Jane Smith, 23, 123 Fake St
#Slim Dusty, 44, 564 Cunnamulla Fella St
#Albus Dumbledore, 100, Hogwarts

peopleD = {
            "Jane Smith":
                {
                "Address": "123 Fake St",
                "Age": 23},
            "Slim Dusty":
                {"Age":44}
            
}

peopleL = {
            "people": [
                {"Name":"Jane Smith",
                "Age": 23,
                "Address": "123 Fake St"},
                {"Name":"Slim Dusty",
                "Age":44}
            ]
            
}

print(peopleD)
#print(peopleD["Slim Dusty"])

for person in peopleD.keys():
    print(person)