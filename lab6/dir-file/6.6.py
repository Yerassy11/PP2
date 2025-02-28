import os
import string
def alphabet_files():
    for file in string.ascii_uppercase:
        with open(f"{file}.txt",'w') as f:
            f.write(f"Это файл {file}.txt\n")
