from pathlib import Path


def seq_ping():
    print('OK!')


def seq_read_fasta(filename):
    file_contents = Path(filename).read_text()
    file_body = file_contents.split('\n', 1)
    file_body = file_body[1].replace('\n', '')
    char = 0
    while char <= 19:
        print(file_body[char])
