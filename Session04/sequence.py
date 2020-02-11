from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "ADA.txt"

# -- Constant with the new of the file to open
file_contents = Path(FILENAME).read_text()

# -- Split the file into two parts, the sequence and the header
file_body = file_contents.split('\n', 1)

# -- We replace the line-jump with an empty character
file_body = file_body[1].replace('\n', '')

# -- Print the number of bases on the console
print("The number of bases is:", len(file_body))
