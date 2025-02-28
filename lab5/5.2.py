import re
text="abb ab abbbb a"
words=text.split()
for i in words:
    if re.match(r"^ab{2,3}",i):
        print(i)