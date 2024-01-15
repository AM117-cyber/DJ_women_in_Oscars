import json
import re

# Define the category groups
category_groups = {
    'writing': ['best book of a musical'],
    'program': ['best play', 'best revival of a play', 'best musical', 'best revival of a musical'],
    'music': ['best original score', 'best sound design of a play', 'best sound design of a musical'],
    'directing': ['best direction of a play', 'best direction of a musical']
}

# Initialize the filtered awards dictionary
filtered_awards = {}

# Open the input JSON file
with open('tonys.json', 'r') as f:
    awards = json.load(f)

    # Iterate over the years and categories in the awards dictionary
    for year, categories in awards.items():
        for category, info in categories.items():
            # Convert the category to lowercase
            category = category.lower()

            # Check if the category belongs to any of the groups
            for group, group_categories in category_groups.items():
                if any(group_category in category for group_category in group_categories):
                    # If it does, add it to the filtered awards dictionary
                    filtered_awards.setdefault(year, {}).setdefault(group, {})[category] = info

# Write the filtered awards to the output JSON file
with open('tonys_data.json', 'w') as f:
    json.dump(filtered_awards, f, indent=4)
