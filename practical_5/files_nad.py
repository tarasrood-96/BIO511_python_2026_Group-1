### Practical 5, File manipulation (in Python)
### w42, 12.10.2026, Monday, 4202 ALC, Hus 4

### Exercises

##.# File manipulation

# import csv
# import os
# import sys

# filename = 'file_manipulation_nad.csv'

# Part 1: Create a CSV file with 5 rows and 5 columns using with open()

# (only if the file doesn't exist yet, so earlier appended rows are kept)

# if not os.path.exists(filename):
#     with open(filename, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(["name", "scientific_name", "length_m", "speed_km/h", "conservation_status"])
#         writer.writerow(["shortfin mako shark", "Isurus oxyrinchus", 4.0, 74.0, "Endangered"])
#         writer.writerow(["salmon shark", "Lamna ditropis", 3.0, 72.4, "Least Concern"])
#         writer.writerow(["blue shark", "Prionace glauca", 3.1, 69.0, "Near Threatened"])
#         writer.writerow(["great white shark", "Carcharodon carcharias", 6.1, 54.7, "Vulnerable"])

#.## Part 2: Append a row from the user's command-line input (sys.argv)

# new_row = sys.argv[1:]  # skip the script name

# if len(new_row) == 5:   # make sure the user gave all 5 columns
#     with open(filename, 'a', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(new_row)
# elif len(new_row) > 0:
#     print("Please give 5 values: Name, Scientific name, Length, Speed, Conservation status")

# elif len(new_row) > 0: # prints the warning only if the user gave the wrong number
# of values. Running with no values at all just creates the file quietly.

# Example, how to append a row from the user's command-line input (sys.argv):

# python files_nad.py "grey reef shark" "Carcharhinus amblyrhynchos" 1.9 49.9 "Endangered"

# More sharks from the world's 10 fastest, ordered by maximum speed, that could be added:
# (python files_nad.py) "grey reef shark" "Carcharhinus amblyrhynchos" 1.9 49.9 "Endangered"
# (python files_nad.py) "common thresher shark" "Alopias vulpinus" 6.1 48.3 "Vulnerable"
# (python files_nad.py) "nurse shark" "Ginglymostoma cirratum" 3.0 40.2 "Vulnerable"
# (python files_nad.py) "bull shark" "Carcharhinus leucas" 3.4 40.2 "Vulnerable"
# (python files_nad.py) "great hammerhead" "Sphyrna mokarran" 6.1 32.2 "Critically Endangered"
# (python files_nad.py) "tiger shark" "Galeocerdo cuvier" 5.0 32.2 "Near Threatened"

# Fun fact: there are more than 500 known shark species in the world today.

# Print the CSV file as an aligned table in the terminal using pandas (run
# without the "#"):
# python -c "import pandas as pd; print(pd.read_csv('file_manipulation.csv'))"

# What the command does, piece by piece

# Part
# python -c "..."
# Meaning
# Run the Python code inside the quotes directly, without needing a .py file (-c = “command”)

# Part
# import pandas as pd
# Meaning
# Load pandas under the short name pd (the usual convention)

# Part
# ;
# Meaning
# Separates two Python statements on one line (instead of a new line)

# Part
# pd.read_csv('file_manipulation.csv')
# Meaning
# Read the CSV and turn it into a DataFrame (a table with rows and columns)

# Part
# print(...)
# Meaning
# Show that table in the terminal

# Note the quotes: double quotes " around the whole Python code, single quotes ' around
# the file name inside. If you used " for both, the terminal would think the code ended early.

# In your output, the numbers 0, 1, 2, 3, 4 on the left are not in your file.
# That’s the index pandas adds to number the rows.

# Will a long file scroll forever?

# No. Pandas protects you from that. If a table has more than 60 rows, print()
# shows only the first 5 and last 5 rows with ... in between, plus a line
# like [200 rows x 5 columns].

# So the problem is actually the opposite: you won’t see everything. Depending
# on what you want:

# See only the first rows (like head):
# python -c "import pandas as pd; print(pd.read_csv('file_manipulation.csv').head(10))"

# See all rows, page by page (scroll with the arrow keys, q to quit):
# python -c "import pandas as pd; print(pd.read_csv('file_manipulation.csv').to_string())" | less -S

# .to_string() turns off the shortening so every row is printed. less -S stops
# the output from rushing past and keeps long lines from wrapping.

##################################################################################################

##.## Arguments and pandas

# import argparse
# import csv
# import pandas as pd

# 1. Create the parser with a description of the script
# parser = argparse.ArgumentParser(
#     description="Read a CSV file of sharks and print a statistical summary of the data."
# )

# 2. Add the input file argument with a help message
# parser.add_argument(
#     "--file",
#     required=True,
#     help="Path to the CSV file to read, e.g. file_manipulation_nad.csv"
# )

# 3. Parse the arguments
# args = parser.parse_args()

# Read the CSV file with the csv module
# with open(args.file, "r", newline="") as csv_file:
#     reader = csv.reader(csv_file, delimiter=",")
#     rows = list(reader)

# header = rows[0]    # first row = column names
# data = rows[1]      # all other rows = the data

# Convert the data to a pandas DataFrame
# df = pd.DataFrame(data, columns=header)

# The csv module reads everything as text, so turn the
# number columns into numbers
# df["length_m"] = pd.to_numeric(df["legnth_m"])
# df["speed_km/h"] = pd.to_numeric(df["speed_km/h"])

# print(df)
# print()
# print("Statistical summary:")
# print(df.describe())

# To include the text columns in the summary as well
# (for example, which conservation status is most
# common), use
# print(df.describe(include="all"))
# instead.

# Run it

# python arguments_pandas_nad.py -h
# python arguments_pandas_nad.py --file file_manipulation_nad.csv

# The summary you should get:

#        length_m  speed_km/h
# count  5.000000     5.00000
# mean   3.620000    64.00000
# std    1.573849    10.96426
# min    1.900000    49.90000
# 25%    3.000000    54.70000
# 50%    3.100000    69.00000
# 75%    4.000000    72.40000
# max    6.100000    74.00000

##################################################################################################

## --- Mini FASTA toolkit with Biopython ---

# In this exercise you will use three parts of Biopython: Seq, SeqRecord and SeqIO.


# - Create the input file -

# Created input file dna_nad.fasta with sequences in the same folder as my script.


# -- Load and report --

# Use SeqIO for this task.