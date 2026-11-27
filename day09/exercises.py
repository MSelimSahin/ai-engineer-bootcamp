from day05.iris_analysis import load_csv
from day08.models import KNNClassifier, NearestCentroidClassifier
def invert_dict(dictionary: dict) -> dict:
    new_dict =  {y: x for x, y in dictionary.items()}
    if len(new_dict) != len(dictionary):
        raise ValueError("Values must be unique to invert the dict")
    return new_dict

def unique_labels(rows):
    return {row[-1] for row in rows}

def min_max_scale(values):
    minimum = min(values)
    maximum = max(values)
    new = [(value - minimum) / (maximum - minimum) for value in values]
    if maximum - minimum == 0:
        raise ZeroDivisionError("max - min must not be 0")
    return new

def make_model(name, **kwargs):
    MODELS = {"knn": KNNClassifier, "nc": NearestCentroidClassifier}
    if name not in MODELS:
        raise ValueError(f"name is not in models. Available models: {MODELS.keys()}")
    model = MODELS[name]
    return model(**kwargs)

if __name__ == "__main__":
    print(invert_dict({"a": 1, "b": 2, "c": 3}))
    header, rows = load_csv("day05/iris.csv")
    print(unique_labels(rows))
    print(min_max_scale([10, 20, 30]))
    print(make_model("knn", k=5))
    print(make_model("svm"))