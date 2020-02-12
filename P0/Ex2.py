from Seq0 import *

DNA_folder = '/home/alumnos/gregocr/PycharmProjects/2019-2020-PNE-Practices/Session04/'
filename = 'U5.txt'
print('DNA file: ', filename)
print('The first 20 bases are', seq_read_fasta(DNA_folder + filename)[0:20])
