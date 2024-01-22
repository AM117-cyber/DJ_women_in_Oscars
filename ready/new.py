import json
# Assuming data is your dictionary
with open('oscar_general.json', 'r') as f:
      data = json.load(f)
with open('output.txt', 'w') as f:
    for year, categories in data.items():
        for category, staff_members in categories.items():
            for staff_member, details in staff_members.items():
                if details['gender'] == 'female':
                    f.write(f"{staff_member}, {details['name_of_work']}, {year}, {category}\n")


# # Assuming data is your dictionary
# with open('oscar_specific_categories.json', 'r') as f:
#      data = json.load(f)
# with open('output.txt', 'w') as f:
#     for year, categories in data.items():
#         for category, staff_members in categories.items():
#             works = {}
#             for staff_member, details in staff_members.items():
#                 work = details['name_of_work']
#                 winner = details['winner']
#                 if work not in works:
#                     works[work] = {'winner': winner, 'staff_member': staff_member}
#                 else:
#                     if works[work]['winner'] != winner:
#                         f.write(f"{works[work]['staff_member']}, {staff_member}\n")
