from day08.models import NearestCentroidClassifier, KNNClassifier
from day05.iris_analysis import train_test_split, load_csv

def leave_one_out(model, rows):
    true_count = 0
    for idx, row in enumerate(rows):
        rows.remove(row)
        prediction = model.fit(rows[:-1]).predict(row[:-1])
        if prediction == row[-1]:
            true_count += 1
        rows.insert(idx, row)
    return f"Accuracy: {true_count / len(rows):.2f}%"

if __name__ == "__main__":

    models = [NearestCentroidClassifier(), KNNClassifier(1), KNNClassifier(3), KNNClassifier(5), KNNClassifier(15)]

    header, rows = load_csv("day05/iris.csv")
    train, test = train_test_split(rows)

    for model in models:
        print(f"{repr(model)}: {model.fit(train).score(test)}")
        print(leave_one_out(model=model, rows=rows))
        print("-" * len(model.__class__.__name__))

    print(f"{repr(KNNClassifier(51))}: {model.fit(train).score(test)}")
    print(leave_one_out(model=KNNClassifier(51), rows=rows))