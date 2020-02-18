from Seq0 import *


DNA_folder = '/home/alumnos/gregocr/PycharmProjects/2019-2020-PNE-Practices/Session04/'
filename = ['ADA', 'U5', 'FXN', 'FRAT1', 'RNU6_269P']
bases = ['A', 'C', 'T', 'G']
for i in range(len(filename)):
    print('\n Gene', filename[i], 'Most frequent Base:', frequent_genes(DNA_folder+filename[i]))
