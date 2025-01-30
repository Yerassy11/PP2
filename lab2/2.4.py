#Tuples
tuple = ("apple", "banana", "cherry") #not the same breckets with list,unchangable,allows duplicats
print(tuple)



mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #shows the is this tuple,list e.t.c



mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language", "History of Kazakhstan") #indexes also starts from zero
print(mytuple[1]) 


mytuple = ("PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra", "English language")
print(mytuple[::-1]) #Reversing tuple



mytuple =("camry", "Cobalt", "Land Cruiser 470")
for i in mytuple:
    print(i)    #print all elements in the tuple



tuple1 = ("a", "b", "c")
tuple2 = ("d", "e")
tuple3 = tuple1+tuple2
print(tuple3)



tuple1 = ("camry", "Cobalt", "Land Cruiser 470")
tuple2 = tuple1 * 2
print(tuple2)