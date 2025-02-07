def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [10, 15, 3, 7, 9, 2]
primes = list(filter(lambda x: is_prime(x), numbers))
print("Простые числа:", primes)
