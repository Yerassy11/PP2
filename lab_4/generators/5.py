n=int(input())
def dicr(n):
    for i in range(n,-1,-1):
        yield i
        
for i in dicr(n):
    print(i)