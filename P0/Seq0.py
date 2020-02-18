from pathlib import Path


def seq_ping():
    print('OK!')


def seq_read_fasta(filename):
    filename += '.txt'
    file_contents = Path(filename).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    return file_body


def seq_len(seq):
    seq += '.txt'
    file_contents = Path(seq).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    return len(file_body)


def seq_count_base(seq, base):
    seq += '.txt'
    count = 0
    file_contents = Path(seq).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    for i in range(0, len(file_body)):
        if file_body[i] == base:
            count = count + 1
    return count


def seq_count(seq):
    seq += '.txt'
    bases = ['A', 'C', 'T', 'G']
    tot = []
    file_contents = Path(seq).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    for i in range(len(bases)):
        count = 0
        for j in range(len(file_body)):
            if file_body[j] == bases[i]:
                count += 1
        tot.append(count)
    return dict(zip(bases, tot))


def seq_reverse(seq):
    seq += '.txt'
    file_contents = Path(seq).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    reversed_str = ''
    for i in range(20):
        reversed_str += file_body[19-i]
    return reversed_str


def seq_complement(seq):
    seq += '.txt'
    op_bases1 = ['A', 'T']
    op_bases2 = ['C', 'G']
    file_contents = Path(seq).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    complement_str = ''
    for i in range(20):
        if file_body[i] == op_bases1[0]:
            complement_str += file_body[i].replace(file_body[i], op_bases1[1])
        elif file_body[i] == op_bases1[1]:
            complement_str += file_body[i].replace(file_body[i], op_bases1[0])
        elif file_body[i] == op_bases2[0]:
            complement_str += file_body[i].replace(file_body[i], op_bases2[1])
        else:
            complement_str += file_body[i].replace(file_body[i], op_bases2[0])
    return complement_str


def frequent_genes(seq):
    seq += '.txt'
    bases = ['A', 'C', 'T', 'G']
    file_contents = Path(seq).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    max_n = 0
    gene = ''
    for i in range(len(bases)):
        count = 0
        for j in range(len(file_body)):
            if file_body[j] == bases[i]:
                count += 1

        if count > max_n:
            gene = bases[i]
            max_n = count
    return gene
