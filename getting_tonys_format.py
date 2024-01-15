# # Open the input and output files
# with open('tonys_all.txt', 'r') as infile, open('tonys_data.txt', 'w') as outfile:
#     # Read the file line by line
#     for line in infile:
#         # Strip leading/trailing white space
#         line = line.strip()
#         # If line is not empty, write the line to the output file
#         if line:
#             outfile.write(line + '\n\n')
import json
import re

# Initialize variables
awards = {}
current_year = ''
current_category = ''
current_content = ''

# Open the input file
with open('tonys_data.txt', 'r') as f:
    for line in f:
        line = line.strip()

        # Match year and category
        match = re.match(r'(\d{4}) Tony Award (.*)', line)
        if match:
            # If there is content from the previous category, save it
            if current_content and current_year and current_category:
                awards.setdefault(current_year, {})[current_category] = current_content.strip()
                current_content = ''

            current_year, current_category = match.groups()
            continue

        # If line is not empty, it's part of the content
        if line:
            current_content += line + '\n'

    # Don't forget to save the last set of content
    if current_content and current_year and current_category:
        awards.setdefault(current_year, {})[current_category] = current_content.strip()

# Write to JSON file
with open('tonys.json', 'w') as f:
    json.dump(awards, f, indent=4)
