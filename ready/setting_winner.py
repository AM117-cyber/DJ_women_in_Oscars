# import json

# # Load the data from the JSON files
# with open('oscar_specific_category.json', 'r') as f:
#     file1 = json.load(f)

# with open('oscar_winners.json', 'r') as f:
#     file2= json.load(f)

# # Iterate over the data in file1
# for year in file1:
#     if year in file2:
#         for category in file1[year]:
#             if category in file2[year]:
#                 for staff_member in file1[year][category]:
#                     if staff_member in file2[year][category]:
#                         # If the staff member is in both files, set 'winner' to 'true'
#                         file1[year][category][staff_member]['winner'] = 'true'

# # Write the modified data back to the JSON file
# with open('oscar.json', 'w') as f:
#     json.dump(file1, f, indent=4)

###########################
##create winner grouped####
###########################
import json

# Load the data from your JSON files
with open('oscar_general.json', 'r') as f:
    file1 = json.load(f)

with open('oscar_specific_categories.json', 'r') as f:
    file2 = json.load(f)

# Define your groups
groups = {
    'program': ['SHORT', 'ANIMATED', 'DOCUMENTARY', 'BEST PICTURE'],
    'writing': ['WRITING'],
    'music': ['MUSIC'],
    'directing': ['DIRECTING']
}

# Function to check if a category belongs to a group
def belongs_to_group(category, groups):
    for group, prefixes in groups.items():
        if any(category.startswith(prefix) for prefix in prefixes):
            return group
    return None

# Iterate over the data in file1
for year in file2:
    if year in file1:
        for category in file2[year]:
            print(category)
            group = belongs_to_group(category, groups)
            if group:
                for staff_member in file2[year][category]:
                    if staff_member in file1[year].get(group, {}):
                        # If the staff member is in both files, set 'winner' in file1 to 'winner' in file2
                        file1[year][group][staff_member]['winner'] = file2[year][category][staff_member]['winner']

# Write the updated data back to file1
with open('oscar.json', 'w') as f:
    json.dump(file1, f, indent=4)
