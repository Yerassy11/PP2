import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), snake_str)
print(snake_to_camel("hello_world_example")) 
