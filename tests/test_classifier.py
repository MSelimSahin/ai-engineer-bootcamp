import pytest
from day06.classifier import NearestCentroidClassifier
from day05.iris_analysis import load_csv, train_test_split

def test_predict_before_fit():
    untrained = NearestCentroidClassifier()
    with pytest.raises(RuntimeError):
        untrained.predict([5.0, 3.4, 1.5, 0.2])

def test_round_score():
    header, rows = load_csv("day05/iris.csv")
    train, test = train_test_split(rows)
    acc = NearestCentroidClassifier().fit(train).score(test)
    assert acc == pytest.approx(0.9667, abs=1e-4)

