from Seq1 import Seq

FOLDER = r'C:\Users\Usuario\PycharmProjects\2019-2020-PNE-Practices2\Session04'
FILE = r'\U5'
FILENAME = FOLDER + FILE

s0 = Seq()
seq_file = Seq(s0.read_fasta(FILENAME))
print(f'Sequence: (Length:  {seq_file.len()}) {seq_file}')
print(f'Bases: {seq_file.count()}')
print(f' Rev: {seq_file.reverse()}')
print(f' Comp: {seq_file.complement()}')
