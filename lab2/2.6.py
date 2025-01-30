#Dictionares.Structure that stores items in key-value pairs
my_dict2 = dict(name="Era", age=25, city="London")
print(my_dict2)


#Adding and modifying
person = {"name": "Arman", "age": 30, "city": "New York"}
person["occupation"] = "Engineer"  # Adding a new key-value pair
print(f"After adding occupation: {person}")

person["age"] = 31  # Modifying an existing value
print(person)

#Removing
del person["city"]
print(person) #city:New York is deleted

person.pop("name")


persons={"name":"Era","age":17,"city":"Almighty"}
#For loop in dictionares
for value in persons.values():
    print(value)

# Iterating through key-value pairs (items)

for key, value in persons.items():
    print("Key: {key}, Value: {value}")
    



my_dict = {"a": 1, "b": 2, "c": 3}

my_dict.update({"c": 4, "d": 5})
print(my_dict)  #Updated: {'a': 1, 'b': 2, 'c': 4, 'd': 5}


my_dict.clear()
print(my_dict)  # Output: Cleared: {},empty

