#quicker fruits
data_dict = {}

with open("pub_with_no_beer.txt") as infile:

    line = infile.readline() # reads everything into a list at once
    
    while line:
        #print("Line {}".format(line))
        
        #print(data_dict)
        if line in data_dict:
            data_dict[line] += 1
        else:
            # Initialize this entry
            data_dict[line] = 1

        
        line = infile.readline()
        
#print(data_dict)
 
lonesome_count = data_dict["lonesome\n"]
 
print("Lonesome is here {} times".format(lonesome_count)) 
   
#print(data)

#data_dict = {}
#Big O
#for word in data:
#    print(word)
#    print(data_dict)
#    if word in data_dict:
#        data_dict[word] += 1
#    else:
#        data_dict[word] = 1

#print(data_dict)