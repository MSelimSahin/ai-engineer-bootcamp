import random
# a) FizzBuzz
for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# b) question A in the exam
numbers = [1, 10, 3, 12, 21, 7]

largest = random.choice(numbers)
second = random.choice(numbers)

# or we could set second to float("-inf")
# second = float("-inf")

for item in numbers:
    if item > largest or largest == second:
        second = largest
        largest = item
    elif item < largest and second < item:
        second = item

    print(largest, second)

# c) question D in the exam
a = [1, 2, 3]
b = [4, 5, 6]

if len(a) != len(b):
    print("These lists can't be dot producted. Because of their lengths.")
else:
    total = 0
    idx = -1
    for x in a:
        idx += 1
        total += x * b[idx]

    print(total)
