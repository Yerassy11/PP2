#Set
# add() adds a single element.
# update() adds multiple elements from an iterable (like a list or another set).
# remove() removes a specific element (raises an error if the element is not present).
# discard() removes a specific element (does nothing if the element is not present).
# pop() removes and returns an arbitrary element.

# Example demonstrating each set keyword/method

my_set = {1, 2, 3}

# add():
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# update(): Adds multiple elements from an iterable
my_set.update([5, 6], {7,8}) # List and set as input
print(my_set)  # Output: update: {1, 2, 3, 4, 5, 6, 7, 8}

# remove(): Removes a specific element (raises KeyError if not found)
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6, 7, 8}


# pop(): Removes and returns an arbitrary element (raises KeyError if empty)
popped_element = my_set.pop()
print(my_set)  # Output: {2, 4, 5, 6, 7, 8}, popped element: 1 (The order is not guaranteed)

# clear(): Removes all elements
my_set.clear()
print(my_set)  # Output: set()

