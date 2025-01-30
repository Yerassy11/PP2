#Operators

# Addition: +
# Multiplication: *
# Subtraction: -
# Divide: /
# Moduls: %
# Exponentiation: **
# Floor division: //

a=2
b=3
c=a+b
print(c)#output:5
d=a*b #d=6
e=a-b #e=-1
f=b/a #f=1.5
g=a**b #g=2**3=8
h=b%a #h=1
i=b//a #i=1,not hte same as b/a(1.5)




# Equal: ==
# Not equal: !=
# Greater than: >
# Greater than or equal: >=
# Less than: <
# Less than or equal: >=

u = int(input())
i = int(input())

if u > i: 
    print("u is greater than i")
elif i > u: 
    print("i is greater than u")
elif u == i: 
    print("u equals i")
elif u!=i:
    print("u isn't equal to i")
else: 
    print("ERROR")
    
#Python Logical Operators:

# AND: Returns True if both statements are true
# OR:  Returns True if one of the statements is true
# NOT: Reverse the result, returns False if the result is true

n=int(input())
m=int(input())
if n==1 and m==1:
    print("n and m is 1")
elif n==1 or m==1:
    print("n or m is 1")
elif not(n)==1 and not(m)==1:
    print("n and m isn't equal to 1")