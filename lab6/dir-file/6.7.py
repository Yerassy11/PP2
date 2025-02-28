import os

def copy_file(source,new_src):
    with open(source,'r') as src,open(source,'w') as nsrc:
        nsrc.write(src.read())