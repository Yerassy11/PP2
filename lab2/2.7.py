#If-Else

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b


#Here some simple exercises for if else
#Check if a number is divisible by 3.
t = int(input())
if t%3 == 0: 
    print("Number is divisible by 3")
else: 
    print("Number is not divisible by 3")
    

# Determines if a number is positive, negative, or zero.
w = int(input())
if w > 0: 
    print("Number is positive")
elif w < 0: 
    print("Number is negative")
else: 
    print("Number is zero")
w = int(input())
if w > 0: 
    print("Number is positive")
elif w < 0: 
    print("Number is negative")
else: 
    print("Number is zero")
    
    
#Compare two integers and find the larger one.
e = int(input())
r = int(input())
if e > r: 
    print("e is greater than r")
elif r > e: 
    print("r is greater than e")
else: 
    print("e and r are equal")
    
    


#Minimum of Two Numbers
a = int(input())
b = int(input())
if a > b: 
    print(a)
else: 
    print(b)
    
    
    
#Age Group
age = int(input())
if age < 13: 
    print("Child")
elif age > 13 and age < 19: 
    print("Teen")
else: 
    print("Adult")
#Palindrome
w = int(input())
if w == w[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")