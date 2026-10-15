### Practical 2

### 14.10.2026 (07.10.2026)

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

sequence = 'GATTACAGAACTGATAC'
count_a = 3     # which A we're looking for

# while loop
a_count = 0     # how many A's we've seen
position = 0
while a_count < count_a and position < len(sequence):   # position < len(sequence); added to make the while loop save
   if sequence[position] == "A":
      a_count += 1
   position += 1
print(position - 1)

# for loop
count2_a = 0
for index, base in enumerate(sequence):
   if base == "A":
      count2_a += 1
      if count2_a == count_a:
         print(index)
         break

# Q: What happens if you look for the tenth A in the sequence?

# A: If you set count_a = 10, the while loop crashes with an error,
# because the 10th A never appears.
# The for loop just finishes quietly and prints nothing, because
# for stops by itself at the end of the sequence.

############################################################

## --- Nested loops ---

# Example code

sequences = ['ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT',
             'CAGTAGTACTCAGT', 'GGTATGCTAGACGAGATCTAATA']
codons = ['CCA', 'TGT', 'GTA', 'TAG']

for sequence in sequences:
   for codon in codons:
      if codon in sequence:
         print(codon + " is in " + sequence)

# See if you can follow every line and work out how this example code works.

# A: For each sequence loop through the list of codons.
# If there is a codon in the sequence, print which codon
# is in which sequence.

# A (Claude): The outer loop picks one sequence at a time,
# and for that sequence the inner loop checks all four
# codons before moving on to the next sequence.
# codon in sequence checks whether the three letters appear
# anywhere in the string, and only matches are printed.


# nested for loop which looks for start and stop codons in sequences

st_codons = ['ATG', 'TAA', 'TAG', 'TGA']
seq_with_st_codons = []

for sequence in sequences:
   found = []
   for codon in st_codons:
      if codon in sequence:
         found.append(codon)
         print(codon + " is in " + sequence)

   has_start = 'ATG' in found
   has_stop = 'TAA' in found or 'TAG' in found or 'TGA' in found
   if has_start and has_stop:
      seq_with_st_codons.append(sequence)
      print(f"{sequence} has both a start and a stop codon")

print(seq_with_st_codons)

# Q: Which sequences have both a start and a stop codon?

# A: 'ATCTGAGTCCACACATG', 'GCGTCGTGCGATGTTCACGTTGAT', 'GGTATGCTAGACGAGATCTAATA'


# Find the sequences where the start codon appears before a stop codon

st_codons = ['ATG', 'TAA', 'TAG', 'TGA']
seq_with_st_codons = []
start_before_stop = []

for sequence in sequences:
   found = []
   for codon in st_codons:
      if codon in sequence:
         found.append(codon)
         print(codon + " is in " + sequence)

   has_start = 'ATG' in found
   has_stop = 'TAA' in found or 'TAG' in found or 'TGA' in found
   if has_start and has_stop:
      seq_with_st_codons.append(sequence)
      print(f"{sequence} has both a start and a stop codon")

      start_pos = sequence.find('ATG')
      for stop in ['TAA', 'TAG', 'TGA']:
         if sequence.find(stop, start_pos + 3) != -1:
            start_before_stop.append(sequence)
            break

print(start_before_stop)

# The second argument to .find() says where to start searching,
# so start_pos + 3 means "only look after the ATG". The break
# stops the same sequence from being added twice if it has
# several stop codons after the start.

# Q: Which sequence(s) have a start codon before a stop codon?

# A: 'GCGTCGTGCGATGTTCACGTTGAT', 'GGTATGCTAGACGAGATCTAATA'

############################################################

## ---- Loop through a dictionary ----

# Example:

# Build a simple dict with the keys pat_001, pat_002 and
# pat_003 that has a value each. Here, the values are lists:

data = {
   'pat_001': ['bacZZt98', 'bac889Ytd'],
   'pat_002': ['bac0GFrr'], 
   'pat_003': ['bac889Ytd', 'bacFq55Hj', 'bacZZt98']
}

# Loop through the dict printing each key and each value as a list.

# for key_patient, value_bact_list in data.items():
#    print(key_patient)
#    print(value_bact_list)

# .items() is what lets you get both the key and the value in each
# round of the loop

# data.keys(); only keys
# data.values(); only values

# add a line to see if the value (list) has the bacterial strain 'bac889Ytd'. 
# If it does it should return 'True'. If not, it should say 'False'.

for key_patient, value_bact_list in data.items():
   print(key_patient)
   print(value_bact_list)
   print('bac889Ytd' in value_bact_list)


# Exercise: reverse the dictionary

# The dictionary data links each patient to a list of bacterial strains.
# In this exercise, you will build the reverse relationship: each
# bacterium should be linked to the patients in which it occurs.

# Work through the following steps. Do not import any additional modules.


# 1. Collect the unique bacteria

# Create an empty list called unique_bacteria.

unique_bacteria = []

# Loop through data and then through each patient’s list of bacteria.
# Add a bacterium to unique_bacteria only if it is not already in
# the list.

# Print the list. It should contain each bacterium once.

# Hint: Use the append() method and an if statement.

for key_patient, value_bact_list in data.items():
   for bacterium in value_bact_list:
      if bacterium not in unique_bacteria:
         unique_bacteria.append(bacterium)
print(unique_bacteria)


# 2. Create the reverse dictionary

# Create an empty dictionary called bacteria_to_patients.

bacteria_to_patients = {}

# Use the list from step 1 to add each unique bacterium as a key.
# Give every key an empty list as its value.

# Hint: To check whether a bacterium is already a dictionary key,
# use if bacterium not in bacteria_to_patients.

for bacterium in unique_bacteria:
   if bacterium not in bacteria_to_patients:
      bacteria_to_patients[bacterium] = []
print(bacteria_to_patients)


# 3. Add the patients to the reverse dictionary

# Loop through data again. For each patient and bacterium, append
# the patient ID to the list belonging to that bacterium.

# Print the completed dictionary.

for key_patient, value_bact_list in data.items():
   for bacterium in value_bact_list:
      if key_patient not in bacteria_to_patients[bacterium]:
         bacteria_to_patients[bacterium].append(key_patient)
print(bacteria_to_patients)