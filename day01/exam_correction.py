# Adding 4 to the last index in the list called x
# 1
x = [1, 2, 3]
y = x
y.append(4)
print(x)

# By default, b=2 so the first print statement will be 6 (3 * 2). The 2nd will be 9 (3 * 3)
# 2
def f(a, b=2):
    return a * b
print(f(3), f(3, 3))

# 1st print is going to be 53 because we're adding strings together. 8 and 3 times "5" is 555
# 3
print("5" + "3", 5 + 3, "5" * 3)

# Even if there is no key in the dictionary given with the get method ("b"), get will create it. But if we said d["b"] it would've occured a KeyError.
# 4
d = {"a": 1}
print(d.get("b", 0))

# 1 to 10 excluding 10, each step is 3, so 1-4-7. Add a " " in between the i's. So it's 1 4 7. And because of this, even number 6 (print statement) is not on a new line, but in the same line and seperated with a " ".
# 5
for i in range(1, 10, 3):
    print(i, end=" ")

# range(6) so it's 0,1,2,3,4,5. not including 6. And because it's a list comprehension = [0, 4, 16] no 36 in the list.
# 6
print([n**2 for n in range(6) if n % 2 == 0])