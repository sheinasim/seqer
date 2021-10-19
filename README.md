# Seqer 
Return .fasta containing records smaller than or larger than desired length.

This script is designed to be run on files in .fasta format 

Dependencies:

* Python3 
* Biopython

> export PATH=$PATH:[PATH TO Seqer]  

### Usage
  
> python short_seqer.py or long_seqer.py \<desired length in bp (integer)\> \<assembly.fasta\>

If no arguments are provided, the script will return help message.

## Outputs

* .fasta file containing sequences shorter or longer than desired length

### Citation

If this script is useful to you, please cite the following in your publication:

```
@software{Seqer,
  author = {Sim, Sheina B.},
  title = {Seqer},
  url = {https://github.com/sheinasim/FindDuplicatesFromBUSCO}
}
```

Sheina B. Sim  
USDA-ARS  
US Pacific Basin Agricultural Research Service  
Hilo, Hawaii, 96720 USA  
sheina.sim@usda.gov  

This script is in the public domain in the United States per 17 U.S.C. § 105
