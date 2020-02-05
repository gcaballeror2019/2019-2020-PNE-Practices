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


with open('dna.txt', 'r') as f:
    tab = ''
    for line in f:
        tab += line.replace("\n", "").replace('"', "").split(",")[0]
    print('The lenght of the DNA sequence is', len(tab))
    print('A:', dna_count(tab)[0], '\n C:', dna_count(tab)[1], '\n T:', dna_count(tab)[2], '\n G:', dna_count(tab)[3])

    f.close()
