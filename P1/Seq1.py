import termcolor
from pathlib import Path

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases='NULL'):
        if strbases == 'NULL':
            self.strbases = 'NULL'
            print('NULL Seq created')
        else:
            codon = ['A', 'T', 'G', 'C']
            valid = True
            for i in strbases:
                if i not in codon:
                    valid = False
            if valid:
                print("New sequence created!")
                self.strbases = strbases
            else:
                print("INCORRECT Sequence detected")
                self.strbases = 'ERROR'

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return '0'
        else:
            return len(self.strbases)


    def count_base(base):
        bases = ['A', 'C', 'T', 'G']
        if base.strbases == 'ERROR' or base.strbases == 'NULL':
            for i in bases:
                print(i,':', 0, end='  ')
        else:
            for i in bases:
                count = 0
                for j in base.strbases:
                    if j is i:
                        count += 1
                print(i, ':', count, end='  ')

    def count(self):
        bases = ['A', 'C', 'T', 'G']
        tot = []
        NumA = 0
        NumC = 0
        NumT = 0
        NumG = 0
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            tot.append(NumA)
            tot.append(NumC)
            tot.append(NumT)
            tot.append(NumG)
            database = dict(zip(bases, tot))
            return database
        else:
            for i in self.strbases:
                if i == 'A':
                    NumA += 1
                elif i == 'C':
                    NumC += 1
                elif i == 'T':
                    NumT += 1
                elif i == 'G':
                    NumG += 1
            tot.append(NumA)
            tot.append(NumC)
            tot.append(NumT)
            tot.append(NumG)
            database = dict(zip(bases, tot))
            return database

    def reverse(self):
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return self.strbases
        else:
            complements = ''
            for i in self.strbases:
                if i == 'A':
                    complements += 'T'
                elif i == 'C':
                    complements += 'G'
                elif i == 'T':
                    complements += 'A'
                elif i == 'G':
                    complements += 'C'
            return complements

    def read_fasta(self, filename):
        filename += '.txt'
        file_contents = Path(filename).read_text()
        dna_string = file_contents.split('\n', 1)
        dna_string = dna_string[1].replace('\n', '')
        return dna_string

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases


def print_seqs(seq_list, colour):
    num_seq = 0
    for i in seq_list:
        ''' We improve the function by adding the 
        termcolor function to add colour to the sequences printed'''
        termcolor.cprint(f'Sequence {num_seq}:(Length: {i.len()}) {i}', colour)
        num_seq += 1


def generate_seqs(pattern, number):
    new_seq = []
    for i in range(number):
        new_seq.append(Seq(pattern*(i+1)))
    return new_seq
