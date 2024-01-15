##############
##adding gender
##############
import json

# Load the data from the JSON files
with open('oscar_specific_category.json', 'r') as f:
    all_nominees = json.load(f)

with open('oscar_women.json', 'r') as f:
    female_nominees = json.load(f)

# Create a set of all female staff members
female_staff = set()
for year, categories in female_nominees.items():
    for category, staff_members in categories.items():
        for staff_member in staff_members.keys():
            female_staff.add(staff_member)

# Iterate over the data in file1 and add the gender property
for year, categories in all_nominees.items():
    for category, staff_members in categories.items():
        for staff_member in staff_members.keys():
            if staff_member in female_staff:
                all_nominees[year][category][staff_member]['gender'] = 'female'
            else:
                all_nominees[year][category][staff_member]['gender'] = 'male'

# Write the modified data back to the JSON file
with open('oscar.json', 'w') as f:
    json.dump(all_nominees, f, indent=4)
