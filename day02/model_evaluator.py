tp = int(input("How much cases correctly predicted as positive?\n"))
fp = int(input("How much cases incorrectly predicted as positive?\n"))
fn = int(input("How much cases that were missed as positive?\n"))
tn = int(input("How much cases correctly predicted as negative?\n"))
total = tp + fp + fn + tn

accuracy = (tp + tn) / total


if tp + fp == 0:
    print("Precision set to 0: the model made no positive predictions.")
    precision = 0
else:
    precision = tp / (tp + fp)

if tp + fn == 0:
    print("Recall set to 0: the model made no positive predictions.")
    recall = 0
else:
    recall = tp / (tp + fn)

# F1 score relies only on tp value. 
if tp == 0:
    print("F1 score set to 0: the model made no positive predictions.")
    f1 = 0
else:
    f1 = 2 * precision * recall / (precision + recall)


print(f"Accuracy: {accuracy:.2f}\nPrecision: {precision:.2f}\nRecall: {recall:.2f}\nF1: {f1:.2f}")

if f1 >= 0.8:
    print("Model is a strong model")
elif f1 >= 0.6:
    print("Model is acceptable")
else:
    print("Model needs work")

if accuracy >= 0.9 and recall < 0.5:
    print("Warning: high accuracy is misleading, the model misses most positives.")