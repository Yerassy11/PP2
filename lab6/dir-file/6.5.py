def write_list(filename,lst):
    with open(filename,'w') as f:
        for i in lst:
            f.write(i)
            
filename="text.txt"
lst=["Hi","My","Bro"]
write_list(filename,lst)