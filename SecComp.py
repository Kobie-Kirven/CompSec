#############
# SecComp: A tool for comparing different secondary structure predictors
#############


#Imports
from fpdf import FPDF
from sequence_comparison import*
from concensus import Concensus
from read_fasta import fasta

#Access list of SSE sequences
fn = open("secondary_structure_sequences.fasta")
lines = fn.readlines()
fn.close()
structure = fasta(lines)

concensus_structure = Concensus(structure)
structure.append(concensus_structure.counts())
###Specify the colors for the different elements 

x = Colors(helix='IndianRed',coil='CornflowerBlue',strand='LimeGreen')
feed = x.get_colors()
chart = Chart(structure,feed)
bits = chart.get_bits()

output = chart.build_chart('test.pdf', feed)







