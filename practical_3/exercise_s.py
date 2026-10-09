# Provided inputs
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Global variables
count = 999
summary = "unset"
result = "unset"

# Count numbers above a limit
def count_above(seq, lim):
    # Local variable
    count = 0
    for num in seq:
        if num > lim:
            count += 1
    return count

print(count)
print(count_above(nums, limit))
print(count)

# Why is the global count still 999, 
# even though the function set a variable called count to 0 and then increased it?
# Pythons autoanswer: The global variable `count` remains 999 because the `count` variable defined inside the `count_above` function is a local variable. In Python, when you assign a value to a variable inside a function, it creates a new local variable that is scoped to that function. This means that the local `count` variable inside `count_above` does not affect the global `count` variable.
# My answer: The global variable does not affect the local variable inside the function. That way, you can have two variables named the same thing, but are assigned different values.

print(" ")

# Summarise a text

def summarize_text(s):
    summary={'digits': 0, 'letters': 0, 'other': 0}
    for character in s:
        if character.isdigit():
            summary["digits"] += 1
        elif character.isalpha():
            summary["letters"] += 1
        else:
            summary["other"] += 1
    return summary

print(summary)
print(summarize_text(text))
print(summary)
print(len(text))

# What counts as "other" in text? 
# Input: text = "Room 101: bring 2 apples & 1 banana."
# Output: {'digits': 5, 'letters': 21, 'other': 10}
# Answer: 'other' is everything else that is not a number or a letter. So other are " ", "&", "." 
# , which are 10 of the in the sentence

# RESULTS:
# unset
# {'digits': 5, 'letters': 21, 'other': 10}
# unset
# 36

print(" ")

# Aggregate with a mode

# # Provided inputs
# nums = [3, -1, 7, 2, 9, 0, 4]
# limit = 4
# text = "Room 101: bring 2 apples & 1 banana."

# # Global variables
# count = 999
# summary = "unset"
# result = "unset"

def aggregate(seq, mode, threshold):
    if mode == "sum" or mode == "count":
        result = 0
    elif mode == "max":
        result = None
    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result:
                    result = n
    return result

print(result)
print(aggregate(nums, "sum", limit))
print(aggregate(nums, "count", limit))
print(aggregate(nums, "max", limit))
print(result)
print(aggregate(nums, "max", 100))

# RESULTS:
# unset
# 20
# 3
# 9
# unset
# None

# The result of print(aggregate(nums, "max", 100)) is None
# This is because results = None due to "max". Then when every number is looped, 
# n will never be above the threshold 100 --> never results = n 
# results stays as None FOREVER

print(" ")

# Errors and try/except

values = ['10', '5', 'hello', '8', 'three', '2', 'omgaaaad', '10.6', '6']

for v in values:
    try:
        print(int(v))
    except ValueError:
        print(f"Skipping invalid value {v} because it's a {type(v).__name__}")