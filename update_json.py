# import json

# # Load the data from the JSON file
# with open('oscar1_0.json', 'r') as f:
#     awards = json.load(f)

# # Iterate over the data and remove staff members named "Story" or "Music"
# for year, categories in list(awards.items()):
#     for category, staff_members in list(categories.items()):
#         for staff_member, details in list(staff_members.items()):
#             # if staff_member.startswith("Eric ") or staff_member.startswith("Jason ") or staff_member.startswith("Tim ") or staff_member.startswith("Michael "):
#              if staff_member in ["Music", "Story"]:
#                  del awards[year][category][staff_member]

# # Write the modified data back to the JSON file
# with open('oscar_winners.json', 'w') as f:
#     json.dump(awards, f, indent=4)


# import json

# # Load the data from the JSON file
# with open('oscar1_0.json', 'r') as f:
#     awards = json.load(f)

# # Initialize a dictionary to hold the short-named staff members
# short_named_staff = {}

# # Iterate over the data and add staff members with short names to the dictionary
# for year, categories in awards.items():
#     for category, staff_members in categories.items():
#         for staff_member, details in staff_members.items():
#             if len(staff_member) <= 7:
#                 if year not in short_named_staff:
#                     short_named_staff[year] = {}
#                 if category not in short_named_staff[year]:
#                     short_named_staff[year][category] = {}
#                 short_named_staff[year][category][staff_member] = details

# # Write the short-named staff members to a new JSON file
# with open('short_named.json', 'w') as f:
#     json.dump(short_named_staff, f, indent=4)


