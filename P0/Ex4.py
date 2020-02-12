from Seq0 import *

DNA_folder = '/home/alumnos/gregocr/PycharmProjects/2019-2020-PNE-Practices/Session04/'
filename = ['ADA', 'U5', 'FXN', 'FRAT1', 'RNU6_269P']
bases = ['A', 'C', 'T', 'G']
for i in range(len(filename)):
    print('\n Gene', filename[i], ': \n')
    for j in range(len(bases)):
        print(bases[j], ': ', seq_count_base(DNA_folder + filename[i], bases[j]))
