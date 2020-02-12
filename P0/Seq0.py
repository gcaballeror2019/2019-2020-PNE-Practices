from pathlib import Path


def seq_ping():
    print('OK!')


def seq_read_fasta(filename):
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
