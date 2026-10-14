### Practical 1

### 14.10.2026 (06.10.2026)

### Exercises

## - Data type usage -

# save an integer to a variable and print that variable

# my_int = 5
# print(my_int)


# make variables with one value for each data type

my_str = "Green dragon"
# my_int = 21
my_float = 1.01
my_bool = True
my_none = None
my_list = [1, 21, 42]
my_dict = {"gene": "lacZ", "length": 42000}
my_tuple = (2, 22, 43)
my_set = {3, 23, 44}
my_range = range(8)

# print(my_str, type(my_str))
# print(my_int, type(my_int))
# print(my_float, type(my_float))
# print(my_bool, type(my_bool))
# print(my_none, type(my_none))
# print(my_list, type(my_list))
# print(my_dict, type(my_dict))
# print(my_tuple, type(my_tuple))
# print(my_set, type(my_set))
# print(my_range, type(my_range))

################################################################

## -- If/Elif/Else on your data types --

# Check how many letters are in my_str. It's the same thing
# as checking the length of a string.

print(len(my_str))


# Create an if/else-statement to determine if the string is
# empty or not. If the string is empty, the length should
# be zero.
# If it’s empty, print “empty”, else print “non-empty”.

if len(my_str) == 0:
    print("empty")
else:
    print("non-empty")

################################################################

# Multi-way (If/elif/else clause)

# Write an if-statement with 3 scenarios (some informative
# text should be printed):
# the integer could be positive,
# the integer could be zero,
# the integer could be negative.

my_int = -2

if my_int > 0:
    print(f"The integer {my_int} is positive.")
elif my_int == 0:
    # x == 0, to compare; x = 0, to define what it is (if it already is
    # sth, it changed after this step) (nicely told by Claude:
    #"== compares, = assigns (and overwrites whatever was there before)")
    print(f"The integer {my_int} is zero.")
else:
    print(f"The integer {my_int} is negative.")

################################################################

# Type gate + nested classification (Nested If/elif/else)

# create a nested if-statement

# make a variable with the sequence and print the variable
my_seq = list("ACTTAGCTAGC")

print(my_seq, type(my_seq))

# a shorter version of outer if, first row: if type(my_seq) in (list, tuple, range):
if type(my_seq) == list or type(my_seq) == tuple or type(my_seq) == range:
    if len(my_seq) == 0:
        print("empty")
    elif len(my_seq) == 1:
        print("single item")
    else:
        print("multiple items")
else:
    print("wrong type for this task")

################################################################

# Look up a sample (dictionaries, in and None)

# A sequencing run produced the dictionary below.

read_counts = {"sample_A": 1520000, "sample_B": 830000, "sample_C": None}

# You can check whether a key exists in a dictionary with in:

print("sample_A" in read_counts)    # prints True



# Save the name of one sample to a variable called sample.

sample = "sample_A"

# Write an if/elif/else statement.

if sample in read_counts:
    if read_counts[sample] is None: # dictionary[key] == None (also works)
        print("sequencing failed")
    elif read_counts[sample] >= 1000000:
        print("enough reads")
    else:
        print("too few reads")
else:
    print("unknown sample")



# Create a variable passed_qc and set it to True.

passed_qc = True

# Change your code so that it prints “ready for analysis” instead of
# “enough reads”, but only if the sample has enough reads and
# passed_qc is True.

if sample in read_counts:
    if read_counts[sample] is None: # dictionary[key] == None (also works)
        print("sequencing failed")
    # elif read_counts[sample] >= 1000000 and passed_qc is True:
    elif read_counts[sample] >= 1000000 and passed_qc:  # more commonly used
        print("ready for analysis")
    elif read_counts[sample] >= 1000000:
        print("enough reads")
    else:
        print("too few reads")
else:
    print("unknown sample")

# Q: What is printed for sample_A when you change passed_qc to False?

# A: When I change passed_qc to False, "enough reads" is printed.