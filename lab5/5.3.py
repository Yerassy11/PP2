import re

pattern = r'[a-z]+_[a-z]+'
test_string = "hello_world,hhellooo,whats_up"

matches = re.findall(pattern, test_string)
print(matches)
