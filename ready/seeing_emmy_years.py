# import re

# def extract_directors(input_file, output_file):
#     with open(input_file, 'r') as f:
#         data = f.readlines()

#     pattern = re.compile(r'\d+\.\s(.*)')
#     directors = [pattern.match(line).group(1) for line in data if pattern.match(line)]

#     with open(output_file, 'w') as f:
#         for director in directors:
#             f.write(director + '\n')

# # Call the function with your input and output file paths
# extract_directors('years.txt', 'output.txt')
import json

def add_gender(json_file, txt_file):
    # Load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Load the names from the text file and convert them to lower case
    with open(txt_file, 'r') as f:
        female_names = [line.strip().lower() for line in f]

    # Add the gender property to each staff member
    for year in data:
        for category in data[year]:
            for staff_member in data[year][category]:
                # Check if the staff member's name begins with one of the female names
                if any(staff_member.lower().startswith(name) for name in female_names):
                    data[year][category][staff_member]['gender'] = 'female'

    # Write the updated JSON data back to the file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

# Call the function with your JSON and text file paths
add_gender('emmys.json', 'output.txt')

