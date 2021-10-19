#!/usr/bin/python

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("maxLength", type=int, help="Maximum length contig retained")
parser.add_argument("fasta", help=".fasta to get sequences from")
args = parser.parse_args()

short_sequences = []

for record in SeqIO.parse(args.fasta, "fasta"):
    if len(record.seq) < args.maxLength:
        short_sequences.append(record)

outfile = args.fasta.split(".fasta")[0] + "_records_shorter_than_" + str(args.maxLength) + ".fasta"       

SeqIO.write(short_sequences, outfile, "fasta")

print("Short seq-er is finished seq-ing.")
