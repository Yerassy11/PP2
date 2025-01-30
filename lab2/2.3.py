#Lists
list=["hello","dear","teacher"]
print(list) #result:['hello', 'dear', 'teacher']
print(len(list)) #output: 3


#A list with strings, integers and boolean values:
list1 = ["che", 18, True, 40, "tam"]


list_nums=[1,2,3,4,5]
print(list_nums[1]) #result will be 1 because list indexes starts from 0

list_new = ["PP1", "PP2", "Calculus 1", "Calculus 2", "History", "Linear algebra"]
print(list_new[:5]) #Result: All elements from 0 to 5(not including). In math can write like this: [0,5)

list = ["PP1", "PP2", "Discra", "Calc 2", "History"]
print(list[3:]) #Result: it will start from 3.

list = ["PP1", "PP2", "Calc 1", "Calc 2", "History", "Linear algebra"]
print(list[-4:-1]) #Result: negative index it means that tarting from at the end of the list. From -4 (including) to -1 (excluding)





#LIST CHANGING
fruits=["apple","banana","watermelon"]
fruits[1]="orange"
print(fruits) #output:[apple","orange","watermelon]

#insert,append
new_fruits=["apple","banana","watermelon"]
new_fruits.insert(0,"mango") #list.insert(index,object)
print(new_fruits) 


nums=[0,2,3,1,3]
nums.append(9)
print(nums) #output:[0, 2, 3, 1, 3, 9] (automatically added object to thew end of the list)



list = ["PP1", "PP2", "Calculus 1"]
list.remove("Calculus 1")
print(list) #Result: in this operation we removed Calculus 1 element from list.


subjects= ["PP1", "PP2", "Calculus 1", "Calculus 2", "Linear algebra"]
subjects.clear()
print(list) #Using clear() we removed all elements from the list.

#SORT
sandar=[1,3,7,4,3,2,9,12,6]
sandar.sort()
print(sandar) #if we put strings in sorts by alphabetically order
