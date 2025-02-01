#Strings
#1
text="I love coding "
print(text)
#2
text = "Hello World"
x = text[0]

#3
text = "Hello World"
x = text[2:5]

#4
text = "Hello World"
x = text.strip()

#5
text = "Hello World"
txt =text.upper()

#6
text = "Hello World"
text=text.lower()

#7
txt = "Hello World"
txt=txt.replace("H","J")

#8
num=36
txt = "My name is Frank Ocean, and I didnt drop  {} years already"
print(txt.format(num))







#-------------------------------------------------------
b = "Hello, World!"
print(b[2:5])
#2
b = "Hello, World!"
print(b[:5])
#3
b = "Hello, World!"
print(b[2:])
#4
b = "Hello, World!"
print(b[-5:-2])

#-----------------------------------------------------------



word = "Python "
print(word * 3)  # Вывод: Python Python Python

#-------------------------------------------------------
#in func
text = "Python programming is fun"
print("Python" in text)  # Вывод: True
print("Java" in text)    # Вывод: False



#----------------------------------------------------------
#count function
text = "Amsterdam"
print(text.count("a")) 