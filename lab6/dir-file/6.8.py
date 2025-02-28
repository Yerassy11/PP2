import os
def delete(path):
    if os.path.exists():
        os.remove(path)
        print("File deleted")
    else:
        print("No such file")
    