from Seq0 import *

DNA_folder = '/home/alumnos/gregocr/PycharmProjects/2019-2020-PNE-Practices/Session04/'
filename = ['ADA', 'U5', 'FXN', 'FRAT1', 'RNU6_269P']
for i in range(len(filename)):
    print('Gene', filename[i], '---> Length:', seq_len(DNA_folder + filename[i]))
