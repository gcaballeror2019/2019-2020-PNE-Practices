from Seq0 import *

DNA_folder = '/home/alumnos/gregocr/PycharmProjects/2019-2020-PNE-Practices/Session04/'
filename = 'U5'
print('Gene', filename)
print('Frag:', seq_read_fasta(DNA_folder + filename)[0:20])
print('Comp:', seq_complement(DNA_folder + filename))