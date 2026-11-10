# There was a misunderstanding yesterday about the get method. Let me correct that. Get doesn't create a key and its value. 
# It just returns it's given value. It doesn't even touch the dictionary. Just returning it.
# 4
d = {"a": 1}
print(d.get("b", 0))

# This is the proof (the code below this)
print(d) # This only gives {'a': 1} not including {'b': 0}

# The main nuance in this question was not append() method. It was aliasing x and y. They both share the same list. Not the copy of it. 
# 1
x = [1, 2, 3]
y = x
y.append(4)
print(x)
print(y) # This will be the same as x whatever is happening.

# This is the proof. Now let's make a copy of x and test it.
y = x.copy()
y.append(5)
print(y)
print(x) # as you see here. It's not the same. They are not sharing the same list. They are different from eachother. y is copied from x. And the list is different. 
# x = [1, 2, 3, 4]
# y = [1, 2, 3, 4, 5]