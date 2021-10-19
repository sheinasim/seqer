#!/usr/bin/python

import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("minLength", type=int, help="Miniimum length contig retained")
parser.add_argument("fasta", help=".fasta to get sequences from")
args = parser.parse_args()

long_sequences = []

for record in SeqIO.parse(args.fasta, "fasta"):
    if len(record.seq) > args.minLength:
        long_sequences.append(record)

outfile = args.fasta.split(".fasta")[0] + "_contigs_more_than_10mb.fasta"       

SeqIO.write(long_sequences, outfile, "fasta")

print("Long seq-er is finished seq-ing.")
