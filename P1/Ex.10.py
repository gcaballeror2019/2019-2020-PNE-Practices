from Seq1 import Seq

folder = r'C:\Users\Usuario\PycharmProjects\2019-2020-PNE-Practices2\Session04'
docs = ['/U5', '/ADA', '/FRAT1', '/FXN', '/RNU6_269P']

for i in docs:
    filename = folder + i
    s = Seq()
    seq_doc = Seq(read_fasta(filename))
    print(f'Gene {i}: Most frequent base: {seq_doc.gene_abundance()}')