from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()

file_header = file_contents.split('\n', 1)

print(file_header[0])
