#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import argparse to allow parsing of files
import argparse
parser=argparse.ArgumentParser(description='Perform BLAST search')

#first parser argument defines what type of BLAST search you wish to perform
parser.add_argument('blasttype', type=str,help='blastn, blastp, blastx, tblastn, tblastx')

#second parser argument defines the fasta file you wish to perform a blast search on
parser.add_argument('fastafile',type=str)

#third argument, the e-value cutoff 
parser.add_argument('evalue',type=float)
args=parser.parse_args()


# In[ ]:


#Import Biopython for use.
import Bio
#Prints the current version number to standard out to confirm the BioPython is installed and loaded correctly.
print("Biopython version is " + Bio.__version__)


# In[ ]:


#Import the necessary modules from Biopython - web NCBI and SeqIO
from Bio.Blast import NCBIWWW
from Bio import SeqIO

#Load the fasta file
fastafile=open(args.fastafile)

#run blast search on sequences provided in our fasta file. This search can be a blastn, blastp, blastx, tblastn, tblastx
result_handle=NCBIWWW.qblast(args.blasttype,'nt',fastafile.read())


# In[ ]:


#creates a new file for saving our results to in xml format
with open("results.xml", "w") as save_file:
    blast_results=result_handle.read()
    save_file.write(blast_results)


# In[ ]:


#Import specific functions for dealing with XML files from the Bio.Blast module.
from Bio.Blast import NCBIXML
#Defines the E-value based on user input.
E_VALUE_THRESH=args.evalue  

for record in NCBIXML.parse(open("results.xml")):
    if record.alignments:
        print("\n")
        print("query: %s" % record.query[:100])
        for align in record.alignments:
            for hsp in align.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    print("match: %s " % align.title[:100])

