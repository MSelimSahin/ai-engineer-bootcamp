# 1) question A in the exam

def second_largest(numbers: list):
    largest = float("-inf")
    second = float("-inf")

    for number in numbers:
        if number > largest:
            second = largest
            largest = number
        elif number != largest and number > second:
            second = number

    if second == float("-inf"):
        return None
    else:
        return second

# 2) question b in the exam

def word_count(sentence):
    word_dict = {}
    sentence = sentence.lower().split()
    for word in sentence:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

# 3) Testing
if __name__ == "__main__":
    assert second_largest([1, 10, 3, 12, 21, 7]) == 12
    assert second_largest([21, 3, 10]) == 10
    assert second_largest([2, 1]) == 1
    assert second_largest([-1, -3]) == -3
    assert second_largest([5, 5, 3]) == 3
    assert second_largest([10, 10, 10]) == None
    assert second_largest([7]) == None

    assert word_count("The cat in the hat") == {"the": 2, "cat": 1, "in": 1, "hat": 1}
    assert word_count("Testing THE funcTions WIth assert") == {"testing": 1, "the": 1, "functions": 1, "with": 1, "assert": 1}