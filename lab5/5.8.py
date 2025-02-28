import re

def split_by_uppercase(text):
    return re.findall(r'[A-Z][a-z]*', text)


print(split_by_uppercase("HelloWorldExample")) 
