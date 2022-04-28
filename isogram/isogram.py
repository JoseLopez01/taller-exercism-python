def is_isogram(string):
    lowercase_string = string.lower()
    for letter in lowercase_string:
        if lowercase_string.count(letter) > 1 and letter.isalpha():
            return False
    return True
