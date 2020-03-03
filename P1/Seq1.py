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

    def count_base(self):
        # --- We divide blank and non-valid inputs from valid ones, then prints the amount of
        # --- bases of each kind
        bases = ['A', 'C', 'T', 'G']
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            for i in bases:
                print(i, ':', 0, end='  ')
        else:
            for i in bases:
                count = 0
                for j in self.strbases:
                    if j is i:
                        count += 1
                print(i, ':', count, end='  ')

    def count(self):
        # --- The program returns a dictionary with the amount of each base
        # --- in the dna string (We separate valid from non-valid inputs)
        bases = ['A', 'C', 'T', 'G']
        tot = []
        num_a = 0
        num_c = 0
        num_t = 0
        num_g = 0
        if self.strbases == 'NULL' or self.strbases == 'ERROR':
            tot.append(num_a)
            tot.append(num_c)
            tot.append(num_t)
            tot.append(num_g)
            database = dict(zip(bases, tot))
            return database
        else:
            for i in self.strbases:
                if i == 'A':
                    num_a += 1
                elif i == 'C':
                    num_c += 1
                elif i == 'T':
                    num_t += 1
                elif i == 'G':
                    num_g += 1
            tot.append(num_a)
            tot.append(num_c)
            tot.append(num_t)
            tot.append(num_g)
            database = dict(zip(bases, tot))
            return database

    def reverse(self):
        # --- The program reverses valid dna strings
        if self.strbases == 'ERROR' or self.strbases == 'NULL':
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        # --- The program finds the reverse sequence of the valid dna strings
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

    def gene_abundance(self):
        # --- Finds the most abundant base in the dna string
        gene_dict = self.count()
        max_gene = max(gene_dict, key=gene_dict.get)
        return max_gene

    def read_fasta(self, filename):
        # --- The program reads a .txt file containing a dna string in which it erase the header and line
        # --- jumps in the text for a clean read
        filename += '.txt'
        file_contents = Path(filename).read_text()
        dna_string = file_contents.split('\n', 1)
        dna_string = dna_string[1].replace('\n', '')
        return dna_string
