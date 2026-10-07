my_str = "Green dragon"
#my_int = 21
my_float = 1.01
my_bool = True
my_none = None
my_list = [1, 21, 42]
my_dict = {"gene": "lacZ", "length": 42000}
my_tuple = (2, 22, 43)
my_set = {3, 23, 44}
my_range = range(8)

print(my_str, type(my_str))
"""print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_bool, type(my_bool))
print(my_none, type(my_none))
print(my_list, type(my_list))
print(my_dict, type(my_dict))
print(my_tuple, type(my_tuple))
print(my_set, type(my_set))
print(my_range, type(my_range))
"""

print(len(my_str))

if len(my_str) == 0:
    print("empty")
else:
    print("non-empty")

my_int = -2

if my_int > 0:
    print(f"The integer {my_int} is positive.")
elif my_int == 0:
    # x == 0, to compare; x = 0, to define what it is (if it already is sth, it changed after this step)(nicer words of Claude:
    #"== compares, = assings (and overwrites whatever was there before)")
    print(f"The integer {my_int} is zero.")
else:
    print(f"The integer {my_int} is negative.")
