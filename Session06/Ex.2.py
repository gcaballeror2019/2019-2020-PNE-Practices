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
    # --- This program allows us to print complete
    # --- sequence lists, showing their lenght

    num_seq = 0
    for i in seq_list:
        print(f'Sequence {num_seq}:(Length: {i.len()}) {i}')
        num_seq += 1


# --- We define a list to check the print_seqs function
seq_list1 = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]


print_seqs(seq_list1)
