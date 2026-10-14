### Practical 0
### 14.10.2026 (05.10.2026)

## Our first python script

# Print "hej"
print("hej!")

# Save a string to a variable and print that variable instead
string_variable = "tardigrade"
print(string_variable)

####################################################################

# -- arguments --

import sys

# use the first and only argument from the user and save it as "input_string"
input_string = sys.argv[1]

# print the input argument
print(input_string)


import sys
import os

# take the path from the user's command-line argument
input_argument = sys.argv[1]

# print just the file name
print(os.path.basename(input_argument))