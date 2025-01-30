#For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
    
#for i in range (start, stop, step)
for i in range(5):  # Generates numbers from 0 to 4 (exclusive of 5)
    print(i)

for i in range(2, 7):  # Generates numbers from 2 to 6 (exclusive of 7)
    print(i)

for i in range(1, 10, 2):  # Generates odd numbers from 1 to 9
    print(i)
    
    
    
    
#Looping with break

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # Exit the loop when num is 3
    print(num)  # Output: 1 2


#Iterating through a dictionary (keys by default)

person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(key, person[key])