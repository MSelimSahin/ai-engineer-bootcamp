# 1) question A in the exam

def second_largest(numbers: list):
    largest = float("-inf")
    second = float("-inf")

    for item in numbers:
        if len(numbers) == 1:
            largest = item
            second = None
        elif item in numbers[item:]:
            if numbers.index(item) == numbers[-1]:
                second = None
            else:
                continue
        elif item == largest:
            second = None
        elif item > largest and second < item:
            second = largest
            largest = item
        elif item > largest:
            largest = item
        else:
            second = None

    return largest, second

numbers = [10, 10, 10]
print(second_largest(numbers=numbers))

# 2) question b in the exam

def word_count(sentence):
    word_dict = {}
    sentence = sentence.lower().split(" ")
    for word in sentence:
        word_dict[word] = word_dict.get(word, 0) + 1
    print(word_dict)

word_count("the cat and the hat")