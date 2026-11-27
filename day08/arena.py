from day08.models import NearestCentroidClassifier, KNNClassifier
from day05.iris_analysis import train_test_split, load_csv

def leave_one_out(model, rows):
    true_count = 0
    for idx, row in enumerate(rows):
        others = rows[:idx] + rows[idx + 1:]
        prediction = model.fit(others).predict(row[:-1])
        if prediction == row[-1]:
            true_count += 1
    return true_count / len(rows)

if __name__ == "__main__":

    models = [NearestCentroidClassifier(), KNNClassifier(1), KNNClassifier(3), KNNClassifier(5), KNNClassifier(15), KNNClassifier(51)]

    header, rows = load_csv("day05/iris.csv")
    train, test = train_test_split(rows)

    for model in models:
        print(f"{repr(model)}: test={model.fit(train).score(test):.4f} loo={leave_one_out(model=model, rows=rows):.4f}\n")