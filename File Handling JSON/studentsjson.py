import json
import csv

#Step 1: Open and read json file
json_file = open("D:\Python Programs\students.json","r")
data = json.load(json_file)
json_file.close()

#Step 2: Open csv file for writing
csv_file = open("D:\Python Programs\students.csv","w",newline='')

#Step 3: Get Headers from json keys
headers = data[0].keys()

writer = csv.DictWriter(csv_file, fieldnames=headers)

#Step 4: Write headers and rows
writer.writeheader()
writer.writerows(data)

#Step 5: Close csv file
csv_file.close()

print("Conversion completed! Check students.csv file")