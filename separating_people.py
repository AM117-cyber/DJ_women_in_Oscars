import json
#la 3 es la que esta bien
# Open the input JSON file
with open('oscar2_0.json', 'r') as f:
    data = json.load(f)

# Initialize the new data dictionary
new_data = {}

# Iterate over the data in the input JSON file
for year, categories in data.items():
    new_data[year] = {}
    for category, people in categories.items():
        new_data[year][category] = {}
        for person, details in people.items():
            # Check if the person string contains ' & '
            if '; ' in person:
                # Split the person string into individual people
                names = person.split('; ')
                for name in names:
                    # Remove trailing ' ' or ' s' from the name
                    name = name.rstrip(' ').rstrip(' s')
                    # Remove leading string followed by 'by ' from the name
                    if ' by ' in name:
                        name = name.split(' by ')[1]
                    # Add the individual to the new data dictionary
                    new_data[year][category][name] = details
            else:
                # Remove trailing ' ' or ' s' from the person
                person = person.rstrip(' ').rstrip(' s')
                # Remove leading string followed by 'by ' from the person
                if ' by ' in person:
                    person = person.split(' by ')[1]
                # Add the person to the new data dictionary
                new_data[year][category][person] = details

# Write the new data to the output JSON file
with open('oscar1_0.json', 'w') as f:
    json.dump(new_data, f, indent=4)

