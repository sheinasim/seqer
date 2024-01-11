#!/usr/bin/python

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("minLength", type=int, help="Miniimum length contig retained")
parser.add_argument("fasta", help=".fasta to get sequences from")
parser.add_argument("-v", "--version", help="Print version.", action="version", version="v1.2")
args = parser.parse_args()

long_sequences = []

for record in SeqIO.parse(args.fasta, "fasta"):
    if len(record.seq) > args.minLength:
        long_sequences.append(record)

outfile = args.fasta.split(".fasta")[0] + "_records_longer_than_" + str(args.maxLength) + ".fasta"

SeqIO.write(long_sequences, outfile, "fasta")

print("Long seq-er is finished seq-ing.")
