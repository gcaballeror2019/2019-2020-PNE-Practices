# -- Session 3, Ex 2

# -- Function which counts each iteration of the four nucleotides


def dna_count(dna):
    a = 0
    c = 0
    t = 0
    g = 0
    for i in range(0, len(dna)):
        if dna[i] == 'A':
            a += 1
        elif dna[i] == 'C':
            c += 1
        elif dna[i] == 'T':
            t += 1
        else:
            g += 1
    return [a, c, t, g]


seq = input('Please enter a valid DNA sequence (A, C, T ,G)')


with open(dna.txt, 'r') as f:
    for line in f:
        Tab = line.replace("\n", "").replace('"', "").split(",")[0]
    print('The lenght of the DNA sequence is', len(Tab))
    print('A:', dna_count(Tab)[0], '\n C:', dna_count(Tab)[1], '\n T:', dna_count(Tab)[2], '\n G:', dna_count(Tab)[3])

    f.close()
