import re

pattern = r'^ab*$'
text="ab abbb aaabbb ass a"
words=text.split()
for i in words:
    if re.match(r"^ab*$",i):
        print (i)
