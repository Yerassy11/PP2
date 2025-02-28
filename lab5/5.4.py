import re
text="Adrian,nIcePeople,blablabla,Hello,HHola"
match=re.findall(r"\b[A-Z][a-z]+",text)
print(match)