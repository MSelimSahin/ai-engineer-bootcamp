import pytest
from day09.exercises import invert_dict, min_max_scale, unique_labels, make_model
from day05.iris_analysis import load_csv
from day08.models import NearestCentroidClassifier
from day09.data import batches

# invert_dict
def test_dict_same_key():
    with pytest.raises(ValueError):
        invert_dict({"a": 1, "b": 1})

def test_dict_normal():
    assert invert_dict({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}

# min_max_scale
def test_min_max_zero():
    with pytest.raises(ZeroDivisionError):
        min_max_scale([5, 5, 5])

def test_min_max_normal():
    assert min_max_scale([10, 20, 30]) == [0.0, 0.5, 1.0]

# unique_labels
def test_unique_labels():
    header, rows = load_csv("day05/iris.csv")
    assert unique_labels(rows) == {'setosa', 'virginica', 'versicolor'}

# make_model
def test_make_model():
    assert make_model("knn", k=5).k == 5

def test_make_model_instance():
    assert isinstance(make_model("nc"), NearestCentroidClassifier) == True

def test_make_model_unknown():
    with pytest.raises(ValueError):
        make_model("svm")

def test_make_model_error():
    with pytest.raises(ValueError):
        make_model("knn", k=0)

# batches
def test_batches_batch_size():
    header, rows = load_csv("day05/iris.csv")
    assert [len(b) for b in batches(rows, 32)] == [32, 32, 32, 32, 22]

def test_batches_sum_batches():
    header, rows = load_csv("day05/iris.csv")
    assert sum([len(b) for b in batches(rows, 32)]) == len(rows)

def test_batches_shuffle():
    header, rows = load_csv("day05/iris.csv")
    copy_rows = rows[:]
    list(batches(rows, 32, shuffle=True))
    assert rows == copy_rows

def test_batches_seed():
    header, rows = load_csv("day05/iris.csv")
    a = list(batches(rows, 32, shuffle=True, seed=1453))
    b = list(batches(rows, 32, shuffle=True, seed=1453))
    assert a == b