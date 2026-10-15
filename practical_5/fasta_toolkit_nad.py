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