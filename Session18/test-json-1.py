import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("person-1.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'First_name', 'Last_name' and 'age'

# -- Read the First_name
first_name = person['First_name']
last_name = person['Last_name']
age = person['age']

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")
print(first_name, last_name)
termcolor.cprint("Age: ", 'green', end="")
print(age)
