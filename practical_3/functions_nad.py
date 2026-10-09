### Example

## Defining a function

# def add_two_numbers(num_one, num_two):
#     number_to_return = num_one + num_two
#     return number_to_return

# Calling the function

# my_added_numbers = add_two_numbers(1, 1)

# print(my_added_numbers) # will print 2

############################################

### Exercises

## Setup

# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

## Count numbers above a limit

def count_above(nums, limit):
    count = 0
    for index, number in enumerate(nums):
        if number > limit:
            count += 1
    return count

print(count)
dans_count_above = count_above(nums, limit)
print(dans_count_above)
print(count)

# Q:
# Why is the global count still 999, even though the function set
# a variable called count to 0 and then increased it?
# A:
# a

## Count numbers above a limit (Claude refined)

def count_above(seq, lim):
    count = 0
    for number in seq:
        if number > lim:
            count += 1
    return count

print(count)
n_count_above = count_above(seq, lim)
print(n_count_above)
print(count)

# For the question, the key idea is scope

# Q:
# Why is the global count still 999, even though the function set
# a variable called count to 0 and then increased it?
# A (Claude):
# The count inside the function is a local variable. It only exists
# while the function runs and is separate from the global count, even
# though they share a name. Changing the local count does not affect
# the global one, so the global count stays 999. The function only
# shares its result with the outside through return.
    # A good way to remember it:
    # each function call gets its own private "box" of variables,
    # which is thrown away when the function finishes. Only the
    # value you return gets out.

#######################################################################

## Summarise a text (Claude assissted)

def summarize_text(s): # Define a function named summarize_text that takes one argument: s.
    summary = {"digits": 0, "letters": 0, "other": 0}
    for element in s:
        if element.isdigit():
            summary["digits"] += 1
        elif element.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

print(summary)
text_summary = summarize_text(text)
print(text_summary)
print(summary)

print(sum(text_summary.values())) # total of the three counts
print(len(text))                  # length of the string
# If the two numbers match, your function counted evey character.
# The counts add up to X, which equals len(text)

# Q:
# What counts as "other" in text? Check that the numbers
# add up to the length of the string using len(text).

# A:
# "Other" is any character that is neither a digit nor
# a letter: spaces, punctuation (., ,, !), symbols (-, #)
# and newlines. Spaces are usually the biggest part.

######################################################################

## Aggregate with a mode

def aggregate(seq, mode, threshold):
    if mode == "sum" or mode == "count":
        result = 0
    elif mode == "max":
        result = None # This means "no qualifying value found yet".
    else:
        raise ValueError("mode must be 'sum', 'count' or 'max'")
    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result == None or n > result:
                    result = n
    return result

print(result)
print(aggregate(nums, "Sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))
print(result)

# else:
#     raise ValueError("mode must be 'sum', 'count' or 'max'")
# This else statement was suggested by Claude:
# Optionally, guard against typos in the mode. If someone
# calls aggregate(nums, "Sum", limit), result is never created,
# and Python crashes with an UnboundLocalError. You could add
# this after your elif mode == "max": branch

# print(aggregate(nums, "max", 100))

# Q:
# What does aggregate(nums, "max", 100) return, and why?

# A:
# It returns None, because no number in nums is >= 100.
# result starts as None and is only replaced when a qualifying
# number is found, so it is never updated.

######################################################################

## Errors and try/except

# example:
number = int('five')
print(number)

# The int() function cannot convert the string 'five' into a number.
# This produces a ValueError.

##.# Handling an error

try:
    number = int('five')
    print(number)
except ValueError:
    print('That is not a valid number.')

##.# Exercise

values = ['10', '5', 'hello', '8', 'three', '2']

for element in values:
    int_element = int(element)
    print(int_element)

# Improvement, naming (Claude)
# Names that describe the data make code easier to read.

for value in values:
    number = int(value)
    print(number)

# Observation: the loop prints 10 and 5, then stops with a
# ValueError at 'hello' because it can't be converted to
# an int.

# Handling an error

for value in values:
    try:
        number = int(value)
        print(number)
    except ValueError:
        print(f'Skipping invalid value: {value}')

# Step 3:
# the loop already continues after an invalid value,
# because try/except is inside the loop, so an error
# only affects the current value.

# Handling an error (Claude improved)

for value in values:
    try:
        number = int(value)
    except ValueError:
        print(f'Skipping invalid value: {value}')
    else:
        print(number)

# Comment:
# keep the try block as small as possible
# It behaves the same here, but it makes clear that only
# int(value) is expeted to fail, and you won't accidentally
# catch errors from other lines.
# Python has an else block for code that should run only
# when no error happened.

# Add another invalid value and check that your code still
# handles it without stopping the loop

values = ['10', 'abc', '5', 'hello', ' 7', '-4', 'separate branch', '8', '3.5', '', 'three', '2']

for value in values:
    try:
        number = int(value)
    except ValueError:
        print(f'Skipping invalid value: {value!r}')
    else:
        print(number)