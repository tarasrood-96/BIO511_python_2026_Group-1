##.## Arguments and pandas

import argparse
import csv
import pandas as pd

# 1. Create the parser with a description of the script
parser = argparse.ArgumentParser(
    description="Read a CSV file of sharks and print a statistical summary of the data."
)

# 2. Add the input file argument with a help message
parser.add_argument(
    "--file",
    required=True,
    help="Path to the CSV file to read, e.g. file_manipulation_nad.csv"
)

# 3. Parse the arguments
args = parser.parse_args()

# Read the CSV file with the csv module
with open(args.file, "r", newline="") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    rows = list(reader)

header = rows[0]    # first row = column names
data = rows[1:]      # all other rows = the data

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=header)

# The csv module reads everything as text, so turn the
# number columns into numbers
df["length_m"] = pd.to_numeric(df["length_m"])
df["speed_km/h"] = pd.to_numeric(df["speed_km/h"])

print(df)
print()
print("Statistical summary:")
print(df.describe())

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