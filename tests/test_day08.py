import pytest
from day08.exercises import majority_vote
from day08.models import KNNClassifier, NearestCentroidClassifier
from day05.iris_analysis import load_csv, train_test_split

# majority_vote
def test_majority_equality():
    assert majority_vote(["a", "b", "a", "b"]) == "a"

def test_majority():
    assert majority_vote(["A", "B", "A", "B", "B"]) == "B"

def test_majority_variety():
    assert majority_vote(["x", "y", "a", "b", "X", "y"]) == "y"

# KNNClassifier
def test_knn_k_zero():
    with pytest.raises(ValueError):
        KNNClassifier(0)

def test_knn_predict_before_fit():
    untrained = KNNClassifier()
    with pytest.raises(RuntimeError):
        untrained.predict([5.0, 3.4, 1.5, 0.2])

# save/load
def test_save_load_roundtrip(tmp_path):
    path = tmp_path / "model.json"
    header, rows = load_csv("day05/iris.csv")
    train, test = train_test_split(rows)
    model = NearestCentroidClassifier().fit(train)
    model.save(path)
    loaded = NearestCentroidClassifier().load(path)
    assert loaded.predict([5.0, 3.4, 1.5, 0.2]) == model.predict([5.0, 3.4, 1.5, 0.2])