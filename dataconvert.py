import csv
import json

csv_file = 'C:/Users/Nick/OneDrive/Desktop/Education/Other Education/Data Analytics/Amsterdam Airbnb/filtered_listings.csv'
json_file = r'C:\Users\Nick\OneDrive\Desktop\Education\Other Education\Data Analytics\Amsterdam Airbnb\filtered_listings.json'  

# Read the CSV file
with open(csv_file, mode='r', newline='', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    rows = list(csv_reader)

# Write to the JSON file
with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(rows, f, indent=4)

print(f"CSV data has been successfully converted to {json_file}")