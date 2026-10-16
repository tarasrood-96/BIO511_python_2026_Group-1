### Practical 5, File manipulation (in Python)

### w42, 15.10.2026, Thursday


## --- Mini FASTA toolkit with Biopython ---

# In this exercise you will use three parts of Biopython: Seq,
# SeqRecord and SeqIO.

from Bio import SeqIO

# - Create the input file -

# Created input file dna_nad.fasta with sequences in the
# same folder as my script.


# -- Load and report --

# Use SeqIO for this task.

# 1. Read all records from the FASTA file
records = list(SeqIO.parse("dna_nad.fasta", "fasta"))

print(f"Number of records: {len(records)}")
print()

# 2. + 3. For each record, print the ID, the sequence
# length and the first 10 bases
for record in records:
    print(f"ID: {record.id}")
    print(f"Length: {len(record.seq)} bp")
    print(f"First 10 bases: {record.seq[:10]}")
    print()

# Run it

# python fasta_toolkit_nad.py

##################################################################

# --- Reverse complements to a new FASTA ---

from Bio.SeqRecord import SeqRecord

rc_records = []

for record in records:
    # 1. Create the reverse complement of the sequence (record.seq is a Seq object)
    rc_seq = record.seq.reverse_complement()

    # 2. + 3. Make a new SeqRecord with the new ID and description
    rc_record = SeqRecord(
        rc_seq,
        id=f"{record.id}_rc",
        description=f"reverse complement of {record.id}"
    )
    rc_records.append(rc_record)

# 4. Write all reverse-complement records to a new FASTA file
count = SeqIO.write(rc_records, "dna_rc_nad.fasta", "fasta")
print(f"Wrote {count} reverse-complement records to dna_rc_nad.fasta")

# Run it and check the file

# python fasta_toolkit_nad.py
# head -6 dna_rc_nad.fasta

##################################################################

# ---- GC% annotation to a new FASTA ----

gc_records = []

for record in records:
    # 1. Calculate the GC% of the sequence
    seq = record.seq.upper()
    gc = 100 * (seq.count("G") + seq.count("C")) / len(seq)

    # 2. Round to 1 decimal place
    gc = round(gc, 1)

    # 3. Create a copy of the record with GC% in the description
    gc_record = SeqRecord(
        record.seq,
        id=record.id,
        description=f"GC={gc}%"
    )
    gc_records.append(gc_record)

# 4. Write the annotated records to a new FASTA file
count = SeqIO.write(gc_records, "dna_with_gc_nad.fasta", "fasta")
print(f"Wrote {count} GC-annotated records to dna_with_gc_nad.fasta")

# Run it and check the headers

# python fasta_toolkit_nad.py
# grep ">" dna_with_gc_nad.fasta

##################################################################

# ----- Translation -----

# 1. Translate each DNA sequence and print the first 10 amino acids
print()
print("Translations (first 10 amino acids):")
for record in records:
    # Trim the sequence to a multiple of 3, so there are no leftover bases
    usable_length = len(record.seq) - len(record.seq) % 3
    protein = record.seq[:usable_length].translate()
    print(f"{record.id}: {protein[:10]}")

# 2. Read dna_rc_nad.fasta back in and check the IDs and descriptions
print()
print("Records in dna_rc_nad.fasta:")
for record in SeqIO.parse("dna_rc_nad.fasta", "fasta"):
    print(f"ID: {record.id} | Description: {record.description}")

# Run it

# python fasta_toolkit_nad.py