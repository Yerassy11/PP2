import os
path='C:\Users\Lenovo\Desktop\pp2\lrn.py\lab6\dir-file'
def check():
    if {os.access(path,os.F_OK)}:
        print("Существует")
    if {os.access(path,os.R_OK)}:
        print("Можно читать")
    if {os.access(path,os.W_OK)}:
        print("Можно писать")
    if {os.access(path,os.X_OK)}:
        print("Можно выполняь")
    