import csv
import json

# Open the CSV file for reading
with open('youtube_data.csv', 'r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(csv_file)

    # Initialize an empty list to store the data
    data = []

    # Iterate through each row in the CSV file
    for row in csv_reader:
        data.append(row)

# Write the JSON data to a file
with open("youtube_data.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)
