n=int(input())
def evens(n):
    for i in range(0,n+1,2):
        yield i
print(", ".join(map(str, evens(n))))
    
    