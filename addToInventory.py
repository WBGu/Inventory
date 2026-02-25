import csv
import json

# File paths
csv_file_path = '2_New_Inventory.csv'
json_file_path = 'Inventory.json'

# 1. Load the existing JSON data
with open(json_file_path, 'r') as json_file:
    inventory_data = json.load(json_file)

# 2. Read the CSV and update the dictionary
with open(csv_file_path, 'r') as csv_file:
    # This replaces tabs with commas on the fly before the CSV reader processes the line
    cleaned_lines = (line.replace('\t', ',') for line in csv_file)
    csv_reader = csv.reader(cleaned_lines)
    
    for row in csv_reader:
        # Clean out any empty strings caused by consecutive delimiters (e.g., a tab next to a comma)
        # and strip extra spaces from the remaining elements
        cleaned_row = [item.strip() for item in row if item.strip()]
        
        # Skip empty rows or malformed rows that don't have both an ID and a Quantity
        if len(cleaned_row) < 2:
            continue 
        
        item_id = str(cleaned_row[0])
        
        # Ensure the quantity is treated as an integer
        try:
            quantity = int(cleaned_row[1])
        except ValueError:
            print(f"Skipping invalid quantity for Item ID {item_id}: '{cleaned_row[1]}'")
            continue

        # 3. Add or update the inventory logic
        if item_id in inventory_data:
            inventory_data[item_id] += quantity
        else:
            inventory_data[item_id] = quantity

# 4. Save the updated data back to the JSON file
with open(json_file_path, 'w') as json_file:
    # indent=4 makes the JSON file readable and formatted nicely
    json.dump(inventory_data, json_file, indent=4) 

print("Inventory.json has been successfully updated!")

# 5. Erase all data in the CSV file
with open(csv_file_path, 'w') as csv_file:
    pass # Opening in 'w' mode automatically truncates the file to 0 bytes

print(f"All data in {csv_file_path} has been successfully erased.")