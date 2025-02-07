from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))