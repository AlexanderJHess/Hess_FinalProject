##Blast Search Script

This is a python script to perform BLAST searches of various kinds utilizing BioPython.
First you need to install Biopython, which can be done from the Bash shell prompt using the following command:

-m pip install biopython --user

##Usage
This program utilizes a parser and is best run from the command line with the following format:
> python (script) (blast type) (fasta file location) (database) (desired e-value)




 
script - This is the .py file of this blast search script

****

blast type - This script utilizes the NCBI qblast, and therefore can perform the following based on the input (e.g. blastn):

blastn - compares DNA query to the NCBI database

blastp - compares a protein query to the protein database

blastx - compares a dna query to a protein database

tblastn - compares a protein query to a DNA database

tblastx - compares a protein encoded in a DNA query to a protein encoded in a DNA database.

*****


database - depending on which type of blast search being performed, different databases have to be used, the following commands are available:

nt	- Nucleotide collection	DNA

nr	- Non-redundant	Protein

refseq_rna	- NCBI Transcript Reference Sequences	DNA

refseq_protein -	NCBI Protein Reference Sequences	Protein

swissprot	- Non-redundant UniProtKB/SwissProt sequences	Protein

pdbaa - protein database	Protein

pdbnt	- nucleotide database	DNA

****

fasta file location - the path to the fasta file you wish to blast.

****

desired e-value - a floating point value to serve as a quality filter. The smaller the value, the more constrained your results will be with respect to quality.

****

so, for example, after maneuvering to the appropriate working directory containing the example fasta file and the python script, from the command line:
> python AJH_BLASTSearch.py blastn testfasta3.fasta nt 0.04


Results

After providing necessary inputs (and assuming an internet connection), the script will perform a blast search and save the results to a file called results.xml in your working directory for posterity. It will then parse the results file and display trimmed results based on your inputted e-value. The trimmed results will display the accession numbers of each file and the identification, organized by each fasta sequence inputted. 
 
