# import csv
# import json

# # Define the groups
# groups = {
#     'program': ['SHORT', 'ANIMATED', 'DOCUMENTARY', 'BEST PICTURE'],
#     'writing': ['WRITING'],
#     'music': ['MUSIC'],
#     'directing': ['DIRECTING']
# }

# # Open the input CSV file
# with open('oscars_all.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)  # Skip the header row

#     # Initialize the awards dictionary
#     awards = {}

#     # Iterate over the rows in the CSV file
#     for row in reader:
#         year, category, name_of_work, staff_members = row

#         # Ignore the category "DOCUMENTARY (Short Subject)"
#         if category == "DOCUMENTARY (Short Subject)":
#             continue
#         if category == "DOCUMENTARY SHORT FILM":
#             continue

#         # Determine the group for the category
#         group = next((g for g, categories in groups.items() if any(category.startswith(c) for c in categories)), None)
#         if group:
#             # Add the data to the awards dictionary
#             if year not in awards:
#                 awards[year] = {}
#             if group not in awards[year]:
#                 awards[year][group] = {}
#             awards[year][group][staff_members] = {'name_of_work': name_of_work, 'winner': False}

# # Write the awards to the output JSON file
# with open('oscar_all.json', 'w') as f:
#     json.dump(awards, f, indent=4)

##################
####No groups#####
##################
import csv
import json

# Define the groups
groups = {
    'program': ['SHORT', 'ANIMATED', 'DOCUMENTARY', 'BEST PICTURE'],
    'writing': ['WRITING'],
    'music': ['MUSIC'],
    'directing': ['DIRECTING']
}

# Open the input CSV file
with open('oscar_winners.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row

    # Initialize the awards dictionary
    awards = {}

    # Iterate over the rows in the CSV file
    for row in reader:
        year, category, name_of_work, staff_members = row

        # Ignore the category "DOCUMENTARY (Short Subject)"
        if category == "DOCUMENTARY (Short Subject)":
            continue
        if category == "DOCUMENTARY SHORT FILM":
            continue

        # Determine the group for the category
        group = next((g for g, categories in groups.items() if any(category.startswith(c) for c in categories)), None)
        if group:
            # Add the data to the awards dictionary
            if year not in awards:
                awards[year] = {}
            if category not in awards[year]:
                awards[year][category] = {}
            awards[year][category][staff_members] = {'name_of_work': name_of_work, 'winner': False}

# Write the awards to the output JSON file
with open('oscar_winner.json', 'w') as f:
    json.dump(awards, f, indent=4)



##################
###Creating csv###
##################

# import csv
# import re

# # Define the categories to consider
# categories_to_consider = ['SHORT', 'ANIMATED', 'DOCUMENTARY', 'MUSIC', 'DIRECTING', 'WRITING', 'BEST PICTURE']

# # Open the input text file
# with open('women_oscars.txt', 'r') as f:
#     lines = f.readlines()

# # Initialize the data list
# data = []
# year = ''
# category = ''

# # Iterate over the lines in the file
# for line in lines:
#     line = line.strip()
#     if re.match(r'\d{4} \(', line):
#         print(line)
#         # This is a year
#         year = line.split(' ')[0]  # Extract the year part before the space
#     elif any(line.startswith(c) for c in categories_to_consider):
#         # This is a category
#         category = line
#     elif ' -- ' in line:
#         # This is a nomination
#         name_of_work, staff_members = line.split(' -- ')
#         data.append([year, category, name_of_work, staff_members])

# # Write the data to the output CSV file
# with open('oscar_women.csv', 'w', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['year', 'category', 'name_of_work', 'staff_members'])  # write header
#     writer.writerows(data)  # write data
