# Reading from a CSV file
import csv

with open('incomee.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Reading from a Text file
with open('output.txt', 'r') as file:
    text_data = file.read()
    print(text_data)

# Reading from a JSON file
# import json

# with open('example.json', 'r') as file:
#     json_data = json.load(file)
#     print(json_data)
