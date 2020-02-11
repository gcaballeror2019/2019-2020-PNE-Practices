from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Constant with the new of the file to open
file_contents = Path(FILENAME).read_text()

# -- Split the dile into two parts, the sequence and the header
file_header = file_contents.split('\n', 1)

# -- Print the contents on the console (Only the header)
print(file_header[0])
