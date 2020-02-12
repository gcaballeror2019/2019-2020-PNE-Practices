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
