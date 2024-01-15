import json
import re

# Define the staff member lines to keep
staff_lines_to_keep = ['Produced by', 'Co-Produced by', 'Executive Producer:', 'Produced in association with', 'Presenting the production by', 'Consulting Producer:', 'This production was originally produced and presented in July 2012 by', 'Originally produced by', 'Originally produced in July 2001 by']

# Open the input JSON file
with open('test.json', 'r') as f:
    awards = json.load(f)

    # Iterate over the years and categories in the awards dictionary
    for year, categories in awards.items():
        if 'program' in categories:
            for subcategory, info in categories['program'].items():
                # Split the info into lines
                lines = info.split('\n')
                # Initialize the new info
                new_info = {}
                for line in lines:
                    # If the line starts with one of the specified strings, extract the staff members
                    for staff_line in staff_lines_to_keep:
                        if line.startswith(staff_line):
                            # Extract the staff members after 'by' or ':'
                            staff_members = re.split(r',|;', line[len(staff_line):].strip())
                            for staff_member in staff_members:
                                # Split the staff member info into name of work, winner status, and staff member info
                                name_of_work, winner_status, staff_member_info = staff_member.split('\n')
                                winner = True if winner_status == 'Winner' else False
                                # Add the staff member to the new info
                                new_info[staff_member_info.strip()] = {'name_of_work': name_of_work, 'winner': winner}
                # Replace the old info with the new info
                categories['program'][subcategory] = new_info

# Write the modified awards to the output JSON file
with open('output1.json', 'w') as f:
    json.dump(awards, f, indent=4)




# # Open the input and output files
# with open('output2.txt', 'r') as infile, open('output1.txt', 'w') as outfile:
#     # Read the file line by line
#     for line in infile:
#         # If the line does not begin with 'Produced by', 'Co-Produced by', or 'Executive Producer:', write it to the output file
#         if not line.startswith(('Produced in association with', 'Presenting the production by', 'Executive Producer:')):
#             outfile.write(line)

# # Open the input and output files
# with open('output.txt', 'r') as infile, open('output1.txt', 'w') as outfile:
#     # Read the file line by line
#     for line in infile:
#         # If the line contains 'prod', write it to the output file
#         if 'Prod' in line:
#             outfile.write(line)

# # Define the categories to keep
# categories_to_keep = ['best play', 'best revival of a play', 'best musical', 'best revival of a musical']

# # Open the input and output files
# with open('tonys_data.txt', 'r') as infile, open('output.txt', 'w') as outfile:
#     # Initialize variables
#     current_category = ''
#     current_info = ''

#     # Read the file line by line
#     for line in infile:
#         # If the line contains 'Tony Award', it's a new category
#         if 'Tony Award' in line:
#             # If the current category is one of the categories to keep, write it and its info to the output file
#             if any(category_to_keep in current_category.lower() for category_to_keep in categories_to_keep):
#                 outfile.write(current_category + '\n' + current_info + '\n')

#             # Start a new category and reset the info
#             current_category = line.strip()
#             current_info = ''
#         else:
#             # If the line is not a new category, it's part of the info for the current category
#             current_info += line

#     # Don't forget to write the last category and its info to the output file
#     if any(category_to_keep in current_category.lower() for category_to_keep in categories_to_keep):
#         outfile.write(current_category + '\n' + current_info + '\n')
