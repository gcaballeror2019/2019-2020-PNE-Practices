import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-Ex01.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
for i in range(3):
    i = str(i+1)
    first_n = 'First_name' + i
    last_n = 'Last_name' + i
    age_n = 'age' + i
    phone_n = 'phone_number' + i

    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person[first_n], person[last_n])
    termcolor.cprint("Age: ", 'green', end="")
    print(person[age_n])
    # Get the phoneNumber list
    phoneNumbers = person[phone_n]

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])