import os
def path_check(path):
    if os.path.exists(path):
        print("Path exists")
        print(f"file name:{os.path.basename(path)}")
        print(f"directory nam: {os.path.dirname(path)}")
    else:
        print("Path is'tn exist")
path_check('C:\\Users\\Lenovo\\Desktop\\pp2\\lrn.py\\lab6\\dir-file')