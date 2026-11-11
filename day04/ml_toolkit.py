# a) metrics
def accuracy(tp, fp, fn, tn):
    total = tp + fp + fn + tn
    if total == 0:
        return 0
    result = (tp + tn) / total
    return result

def precision(tp, fp):
    if tp + fp == 0:
        return 0
    result = tp / (tp + fp)
    return result

def recall(tp, fn):
    if tp + fn == 0:
        return 0
    result = tp / (tp + fn)
    return result

def f1_score(tp, fp, fn):
    if tp == 0:
        return 0
    calculated_precision = precision(tp=tp, fp=fp)
    calculated_recall = recall(tp=tp, fn=fn)
    result = 2 * calculated_precision * calculated_recall / (calculated_precision + calculated_recall)
    return result

# b) Dot product
def dot(a: list, b: list):
    if len(a) != len(b):
        return None
    if len(a) == 0 or len(b) == 0:
        return None
    total = 0
    for idx in range(len(a)):
        total += a[idx] * b[idx]
    return total

# c) Gradient descent
def gradient_descent(start_x, learning_rate, tolerance=1e-6, max_steps=10000):
    steps = 1
    gradient = 2 * start_x + 3
    x = start_x - learning_rate * gradient
    while abs(gradient) >= tolerance and steps < max_steps:
        steps += 1
        gradient = 2 * x + 3
        x = x - learning_rate * gradient

    final_x = round(x, 2)
    return final_x, steps

if __name__ == "__main__":
    learning_rates = [0.01, 0.1, 0.5, 1.0]
    for lr in learning_rates:
        print(gradient_descent(10, lr))

    # d) Testing
    assert round(accuracy(0, 0, 0, 0), 2) == 0

    assert round(precision(0, 0), 2) == 0
    assert round(precision(1, 2), 2) == 0.33

    assert round(recall(0, 0), 2) == 0
    assert round(recall(2, 1), 2) == 0.67

    assert f1_score(0, 2, 6) == 0
    assert f1_score(4, 0, 0) == 1

    assert dot([1, 2, 3], [4, 5, 6]) == 32
    assert dot([], []) == None

    assert gradient_descent(0, 0) == (0, 10000)
    assert gradient_descent(10, 0.1) == (-1.5, 77)


    print("All tests passed!")