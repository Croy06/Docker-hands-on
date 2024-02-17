#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
from collections import Counter

# Create a parser for command line arguments
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')

# Add arguments for sequence and motif
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")
parser.add_argument("-p", "--percentage", action='store_true', help="Calculate nucleotide percentage")

# If no arguments are provided, print help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command line arguments
args = parser.parse_args()

# Convert the sequence to uppercase
args.seq = args.seq.upper()

# Check if the sequence is valid (only contains ACGTU)
if re.search('^[ACGTU]+$', args.seq):
    # If the sequence contains both T and U, it's mutagenic
    if 'U' in args.seq and 'T' in args.seq:
        print('Hold on! The sequence contains both ‘T’ and ‘U’, which is unusual. It might be a sign of a mutagenic sequence.')
    # If the sequence contains T, it's DNA
    elif 'T' in args.seq:
        print('Eureka! The sequence you’ve provided is DNA. It’s the blueprint of life!')
    # If the sequence contains U, it's RNA
    elif 'U' in args.seq:
        print('Interesting! The sequence you’ve entered is RNA. It’s a key player in protein synthesis and gene regulation!')
    # If the sequence contains neither T nor U, it could be either DNA or RNA
    else:
        print("Oops! The sequence you've entered seems to be DNA or RNA.")
# If the sequence is not valid, print an error message
else:
    print("Oops! The sequence you've entered doesn't seem to be valid DNA or RNA. It's like trying to read a book in a language you don't understand.")

# If a motif is provided, search for it in the sequence
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"...', sep = " ")
    # If the motif is found in the sequence, print a success message
    if re.search(args.motif, args.seq):
        print("Great news! The motif you're looking for is present in the sequence. It's like finding a needle in a haystack!")
    # If the motif is not found, print an error message
    else:
        print("I'm sorry, but the motif you're searching for doesn’t appear in the sequence. It's like searching for a four-leaf clover in a field of three-leaf ones.")

def nucleotide_percentage(sequence):
    """
    This function calculates the percentage of each nucleotide in a given sequence.
    It uses the collections.Counter class for efficient counting.
    """
    # Count the nucleotides in the sequence
    nucleotide_counts = Counter(sequence)

    # Calculate the percentages
    total = len(sequence)
    nucleotide_percentages = {nucleotide: count / total * 100 for nucleotide, count in nucleotide_counts.items()}

    return nucleotide_percentages

# If the percentage option is enabled, calculate the nucleotide percentage
if args.percentage:
    print(nucleotide_percentage(args.seq))