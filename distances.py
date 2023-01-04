import csv

# Opens the Distance Table csv file and enters them into the distance_list list with a for loop.
# Time Complexity: O(n)
# Space Complexity: O(n)
with open("Distance Table.csv") as distanceTable:
    reader = csv.reader(distanceTable, delimiter=",", quotechar='"')
    distance_list = list(reader)