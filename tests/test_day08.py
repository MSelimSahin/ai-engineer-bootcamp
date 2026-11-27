import pytest
from day08.exercises import majority_vote, closest_to_origin
from day08.models import KNNClassifier, NearestCentroidClassifier
from day05.iris_analysis import load_csv, train_test_split
from day08.arena import leave_one_out

# majority_vote
def test_majority_equality():
    assert majority_vote(["a", "b", "a", "b"]) == "a"

def test_majority():
    assert majority_vote(["A", "B", "A", "B", "B"]) == "B"

def test_majority_variety():
    assert majority_vote(["x", "y", "a", "b", "X", "y"]) == "y"

def test_majority_empty():
    with pytest.raises(ValueError):
        majority_vote([])

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

# leave_one_out
def test_loo_side_effect():
    header, rows = load_csv("day05/iris.csv")
    copy_rows = [row[:] for row in rows]
    leave_one_out(model=NearestCentroidClassifier(), rows=rows)
    assert copy_rows == rows

# closest_to_origin
def test_cto_n_dimensional():
    assert closest_to_origin([[10, 2], [5, 3, 2], [1, 2, 1, 1]]) == [1, 2, 1, 1]