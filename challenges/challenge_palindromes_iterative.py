def is_palindrome_iterative(word):
    inverted_word = word[::-1]
    if len(word) == 0:
        return False
    elif word == inverted_word:
        return True
    else:
        return False
    raise NotImplementedError
