#csv opener

import csv

with open("deniro.csv") as infile:
    rdr = csv.reader(infile)
    for row in rdr:
        print(row)