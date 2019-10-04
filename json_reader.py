import json

data = {}
with open("people_json.txt") as infile:
    data = json.load(infile)

print(data)