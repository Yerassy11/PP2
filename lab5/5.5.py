import re

pattern = r'^a.*b$'
test_strings = [
    "ab",
    "acb",
    "a123b",
    "b",
    "abc",
    "a\nb" 
]

for s in test_strings:
    if re.match(pattern, s):
        print(s)

