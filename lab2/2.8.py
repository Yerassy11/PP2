#While loops.With the while loop we can execute a set of statements as long as a condition is true
#Python has two primitive loop commands While loops and For loops.

count = 1
while count <= 10:
    print(count)
    count += 1
    
i=0
while i<10:
    print(i)
    


#Summing numbers entered by the user until they enter 0

sum = 0
num = int(input("Enter a number (0 to stop): "))

while num != 0:
    sum += num
    num = int(input("Enter a number (0 to stop): "))

print("The sum is:", sum)




#Looping with a break statement 
i = 0
while i < 10:
    i += 1
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # Output: 1 2 3 


#While loop with an else clause 

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop completed normally.")