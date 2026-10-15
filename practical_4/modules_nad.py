# PRACTICAL 4, MODULES, w41, 11.10.2026 (15.10.2026)

# Q:
# What is the difference between folder and directory?

# A:
# Folder vs. directory: they're the same thing. "Directory"
# is the traditional term used by the file system and
# command line (cd = change directory, mkdir = make
# directory), while "folder" is the visual metaphor used
# in graphical interfaces like your VS code sidebar. Your
# practical_4 is both a folder and a directory.

#####################################################################

## - Explore the codons function -

# Open premade_script.py and find the function called codons.
# main.py imports this function and uses it.

# 1. Using the comments in the function, can you describe what it does?
# (Claude)

# It reads a FASTA file and stores each sequence in a dictionary, with
# the header (the text after >) as the key. Sequences split over
# several lines are joined together. It then splits each sequence into
# codons (pieces of 3 nucleotides) and returns a new
# dictionary: header → list of codons.


# 2. What’s the input of the function? (Claude)

# The path to a FASTA file (sequence_file). In main.py, that path
# comes from the command line through -s, as args.sequence.


# 3. In the main function of main.py, add a print statement to print
# the output of the function. (Claude)

# The print statement. Add it right after the function is called,
# inside main():

# sequence_codons = codons(args.sequence)

# # Here you need to check the output of the function
# print(sequence_codons)

# Then run it with:

# python main.py -s sequences.fa

# You should see something like {'header1': ['ATG', 'GCT', ...], ...}.

######################################################################

## -- Explore the exercise_function --

# Stay in premade_script.py and find the function called exercise_function.

# 1. What’s the input of the function?

# The input of the function is list named codon_list.

# (Claude)
# The input is a list of codons (codon_list), i.e. a list of three-letter
# DNA strings such as ['ATG', 'GCT', 'TTT', 'TAA']. One sequence’s list
# from the output of codons() is exactly that kind of input.


# 2. What does this function do?

# This function translates dna codons into amino acid and saves
# the amino acid sequence as a string in a variable aa_string.

# (Claude)
# The function loops over the codons and translates each one into its
# amino acid, using Biopython’s Seq(codon).translate(). The amino
# acids (one-letter codes, with * for a stop codon) are joined into
# a string, aa_string, which the function returns. In other words,
# it converts a list of codons into a protein sequence.

# “Returns” is the important word here: aa_string isn’t saved
# anywhere you can reach from outside, it’s handed back to whoever
# called the function. That’s also why importing it didn’t
# work earlier.


# 3. Try calling it through main.py. See how the previous function
# is imported and used.

# (Claude)
# Calling it through main_nad.py:

# from premade_script_nad import codons, exercise_function

# Then, in main(), after your print(sequence_codons):

# # Here you need to call the exercise_function from premade_script.py
# for header, codon_list in sequence_codons.items():
#     protein = exercise_function(codon_list)
#     # And check the output of that function
#     print(header, protein)

# The loop is needed because codons() returns a dictionary of lists, one
# per sequence, while exercise_function takes one list at a time. So
# each list is passed in on its own.

# When you run it, you’ll most likely get NameError: name 'Seq' is not
# defined. That’s expected, and it’s exactly what the next
# exercise (“Make the exercise_function work”) is about.

######################################################################

## --- Make the exercise_function work ---

# 1. A non-standard module is needed to run the function.
# Which one? Install and use it.

# Claude
# Biopython. "exercise_function" uses "Seq", which isn’t built into
# Python but comes from Biopython’s "Bio.Seq" module. You already
# have it installed (your "conda list" showed version 1.88), so you
# only need the “use it” part.

# Add this import at the top of "premade_script_nad.py":

# from Bio.Seq import Seq

# It has to go in "premade_script_nad.py", not in "main_nad.py",
# because that’s where "exercise_function" is defined and where
# "Seq" is used. Each file needs its own imports.

# 2. Check the output of the script.

# Claude
# Run it again:

# python main_nad.py -s sequences_nad.fa

# After the codon dictionary, you should get one protein per
# sequence, for example:

# sequence_1_short MAF*
# sequence_2_varied MPEW*
# sequence_3_gc_rich MAA*

# Every protein starts with "M" (methionine, from the start
# codon ATG) and ends with "*", which is how Biopython shows
# a stop codon.

# Look closely at the "mystery_sequence" output and read the
# one-letter amino acid codes as ordinary letters. There’s a
# hidden message in it 🙂

######################################################################

# Claude
# Q: Tack! Is the hidden message "my hover craft is full feels", I
# don't really understand it, what could it mean? Could you please
# explain what -s means in python main_nad.py -s sequences_nad.fa

# A: Almost! It’s “My hovercraft is full of eels”, a famous line from
# a Monty Python comedy sketch. In the sketch, a man uses a deliberately
# wrong phrasebook, so he says absurd sentences like this one instead
# of what he actually means. The Python language is named after Monty
# Python, so programmers like to hide their jokes in code examples.

# Some letters are missing ("MYH_VERCRAFT IS F_LL _F EELS") because
# there are no amino acids with the one-letter codes O or U among the
# standard 20. The person who made the exercise had to leave those
# letters out, since no codon translates to them.

# What "-s" means: it’s a command-line option, also called a flag,
# that "main_nad.py" defines with "argparse":

# parser.add_argument('-s', '--sequence', type=existing_file, required=True, ...)

# That line says:

# "-s" (short form) or "--sequence" (long form) marks the next
# value as the input file. "python main_nad.py --sequence sequences_nad.fa"
# does exactly the same thing.

# The value is stored as "args.sequence", which is why the code
# calls codons(args.sequence).

# "required=True" means the script refuses to run without it.

# "type=existing_file" checks first that the file exists.
# That’s the check that gave you “is not a valid file” earlier.

# Compared with "sys.argv[1]" from your first exercise, named
# flags like "-s" are clearer and let the arguments come in any
# order. "argparse" also gives you a help message for
# free: try "python main_nad.py -h".