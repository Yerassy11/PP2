def is_palindrome(word):
    word = word.replace(" ", "").lower()  # Remove spaces and make lowercase
    return word == word[::-1]

print(is_palindrome('mam'))