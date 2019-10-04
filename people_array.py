#people array

#Jane Smith, 23, 123 Fake St
#Slim Dusty, 44, 564 Cunnamulla Fella St
#Albus Dumbledore, 100, Hogwarts

people = [
            ["Jane Smith",23,"123 Fake St"],
            ["Slim Dusty","564 Cunnamulla Fella St",44],
            ["Albus Dumbledore",100,"Hogwarts"],
        ]

#print(people[0])

for person in people:
    print(person)
    if person[0] == "Slim Dusty":
        print("here he is!")