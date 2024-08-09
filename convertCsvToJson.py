import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Read the CSV file
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each row into a dictionary and add it to the data list
        for row in csv_reader:
            data.append(row)

    # Write the list of dictionaries to a JSON file
    with open(json_file_path, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage
csv_file_path = 'input.csv'
json_file_path = 'output.json'
csv_to_json(csv_file_path, json_file_path)


Example Input (input.csv):
---------------------------
name,age,city
John,23,New York
Anna,22,Boston
Mike,32,Chicago


Example Output (output.json):
------------------------------

[
    {
        "name": "John",
        "age": "23",
        "city": "New York"
    },
    {
        "name": "Anna",
        "age": "22",
        "city": "Boston"
    },
    {
        "name": "Mike",
        "age": "32",
        "city": "Chicago"
    }
]
