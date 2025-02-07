from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))
        
print_permutations("era")







numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]
# Call the filter_prime function
prime_numbers = filter_prime(numbers)

print(prime_numbers)