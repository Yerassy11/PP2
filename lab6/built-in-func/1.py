llist=input("size list:")
new_list=list(map(int,llist.split()))
multiplay=1
for i in new_list:
    multiplay*=i
print(multiplay)