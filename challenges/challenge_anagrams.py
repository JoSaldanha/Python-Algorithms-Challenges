def bubble_sort(word):
    word_list = list(word)
    n = len(word_list)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if word_list[j] > word_list[j + 1]:
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
                swapped = True
        if not swapped:
            break

    return "".join(word_list)


def is_anagram(_first_string, _second_string):
    first_string = _first_string.lower()
    second_string = _second_string.lower()

    sorted_word1 = bubble_sort(first_string)
    sorted_word2 = bubble_sort(second_string)

    if first_string == "" or second_string == "":
        return (first_string, second_string, False)

    if sorted_word1 == sorted_word2:
        return (sorted_word1, sorted_word2, True)
    else:
        return (sorted_word1, sorted_word2, False)

    raise NotImplementedError
