# make a list
# my_list = ["b", "list", "perseverance", "har", "theory", "och", "complex", 72]

# double checking if it's a list
# print(type(my_list))

# print your list
# print(my_list)

# print the first item in the list
# print(my_list[7])

# create a list of 7 items
my_list2 = ["b", "list", "perseverance", "har", "theory", "och", "complex"]

# loop over the list (my_list2), printing each item of the list
#for item in my_list2:
#    print(item)

# for each iteration, print the loop number (index)
# e.g., on the third loop (iteration) it's supposed to print a "3"
#iterations = 0

#for item in my_list2:
#    iterations += 1
#    print(iterations)

# perhaps better version of the latter for loop (Claude)
#for index, item in enumerate(my_list2, start=1):
#    print(index)

# printing enumerated list to see how it looks
print(list(enumerate(my_list2, start=1)))

#Add an if-statement to make the loop stop after printing its 5th item
for index, item in enumerate(my_list2, start=1):
   print(index)
   if index < 5:
      continue
   else:
      break
# continue does nothing here; continue means "skip to the next pass,"
# but the loop would go to the next pass anyway, since nothing comes
# after it

# shorter version of the latter for loop
for index, item in enumerate(my_list2, start=1):
   if index <= 5:
      print(index)
   else:
      break

# refined version of the latter two for loops (Claude)
for index, item in enumerate(my_list2, start=1):
   print(index, item)
   if index == 5:
      break

# while loop, find the position of the third A in the sequence
#sequence = 'GATTACAGAACTGATAC'
#print(type(sequence))
#print(list(enumerate(sequence)))
#a_count = 0

#while a_count < 3:
#   for index, item in list(enumerate(sequence)):
#      if item == "A":
#         a_count += 1
#         print(index)
#   if a_count >= 3:
#      break

#while a_count < 3:
#   if item == "A" in list(enumerate(sequence)):
#      a_count += 1
#   if a_count == 3:
#      print(index)

#for the latter attempt of while loop, a position variable is missing;
#right now there is nothing that moves through the sequence;
#item and index don't exist outside a for loop;
#a while loop doesn't step through anything by itself,
# so you have to do the stepping yourself

# next attempt of the while loop (assissted by Claude)
sequence = 'GATTACAGAACTGATAC'
a_count = 0
position = 0

while a_count < 3:
   if sequence[position] == "A":
      a_count += 1
   position += 1

print(position - 1)

# use for loop to solve the same problem as in the latter while loop

sequence = 'GATTACAGAACTGATAC'
a_count2 = 0

for index, item in list(enumerate(sequence)):
   if item == "A":
      a_count2 += 1
   if a_count2 >= 3:
      print(index)
      break

## refined version (Claude)

sequence = 'GATTACAGAACTGATAC'
a_count3 = 0

for index, base in enumerate(sequence):
   if base == "A":
      a_count3 += 1
      if a_count3 == 3:
         print(index)
         break

# list() isn't needed; for can loop over enumerate(sequence) directly;
# wrapping it in list() was only useful for printing it to see what
# it looks like

# put the second if inside the first
# a_count2 can only reach 3 right after it was increased,
# so you only need to check it when you've just found an A
# You can then also use == instead of >=

# I also renamed item to base.
# Any name works, but naming it after what it actually is
# makes the code easier to read.

## Add a variable in the beginning of the code count_a = 3 and reuse that in both loops

# you can now easily change the value for both loops
# What happens if you look for the tenth A in the sequence?

sequence = 'GATTACAGAACTGATAC'
count_a = 3
position2 = 0

while count_a < 13:
   if sequence[position2] == "A":
      count_a += 1
   position2 += 1

print(position2 - 1)

count2_a = 0

for index, base in enumerate(sequence):
   if base == "A":
      count2_a += 1
      if count2_a == 13:
         print(index)
         break