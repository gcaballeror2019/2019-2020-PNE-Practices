class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
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
        return len(self.strbases)


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


def print_seqs(seq_list):
    num_seq = 0
    for i in seq_list:
        print(f'Sequence {num_seq}:(Length: {i.len()}) {i}')
        num_seq += 1


def generate_seqs(pattern, number):
    # --- We create a new sequence which is formed by n multiples of a pattern of codons given
    new_seq = []
    for i in range(number):
        new_seq.append(Seq(pattern*(i+1)))
    return new_seq


# --- We generate two different sequences of variable lenght (in this case 1 & 2) to check the function
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
