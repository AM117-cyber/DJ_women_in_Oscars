import re

def extract_people(data):
    """Extracts names of people involved in a production from text data."""
    people = []
    lines = data.strip().splitlines()

    patterns = [
        r"(?i)(Presented by|Produced by|Executive Producer:|Consulting Producer:|Originally produced by)(.*):?",
        r"(?i)(Executive Producer: )(.*)",
        r"(?i)(Produced|Presented)(?: in| at)? \d{4} by (.*)",
    ]

    for line in lines:
        for pattern in patterns:
            match = re.match(pattern, line, flags=re.IGNORECASE)
            if match:
                # Extract and clean the name(s)
                names_str = match.group(2)  # Access the second group (names)
                names = re.sub(r"[\(\)\[\],:]", "", names_str).split("and")
                people.extend([name.strip() for name in names if name])  # Skip empty names
                break
        else:
            # Handle the "Produced in association with" case separately
            match = re.match(r"(?:Produced in association with)(.*)", line, flags=re.IGNORECASE)
            if match:
                names_str = match.group(1)  # Access the first (and only) group
                names = re.sub(r"[\(\)\[\],:]", "", names_str).split("and")
                people.extend([name.strip() for name in names if name])  # Skip empty names

    return people

# Example usage
data = """Produced by Manhattan Theatre Club (Lynne Meadow, Artistic Director; Alice, Director)
Co-Produced by Hunter Arnold
Executive Producer: D.S. Moynihan
Produced in association with
Presenting the production by The Public Theater (Oskar Eustis, Writer)
Consulting Producer:
This production was originally produced and presented in July 2012 by
Originally produced by Tectonic Theater Project (Anna, Producer)
Originally produced in July 2001 by The Public Theater / New York Shakespeare Festival (George C. Wolfe: Producer; Michael Hurst: Managing Director)"""

people = extract_people(data)

print(f"People involved: {', '.join(people)}")
