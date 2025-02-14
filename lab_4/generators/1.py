n=int(input())
def square_nums(n):
    for i in range(1,n+1):
        yield i**2
for i in square_nums(n):
    print(i)