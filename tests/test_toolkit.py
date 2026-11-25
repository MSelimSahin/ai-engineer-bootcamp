import pytest
from day04.ml_toolkit import dot
from day05.iris_analysis import distance
from day05.exercises import matmul

# dot tests
def test_dot_sum():
    assert dot([1, 2, 3], [4, 5, 6]) == 32

def test_dot_length_mismatch():
    with pytest.raises(ValueError):
        dot([1, 2], [1, 2, 3])

def test_dot_empty():
    with pytest.raises(ValueError):
        dot([], [])

# distance tests
def test_distance_two_dim():
    assert distance([0, 0], [3, 4]) == 5.0

def test_distance_four_dim():
    assert distance([0, 0, 0, 0], [1, 1, 1, 1]) == 2.0

def test_distance_same():
    assert distance([1, 2, 3, 4], [1, 2, 3, 4]) == 0 

def test_distance_length_mismatch():
    with pytest.raises(ValueError):
        distance([1, 2], [1, 2, 3])

def test_distance_round():
    assert distance([0, 0], [1, 1]) == pytest.approx(1.4142, abs=1e-4)

# matmul tests
def test_matmul_calc():
    assert matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]

def test_matmul_different_lens():
    assert matmul([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]) == [[14, 32], [32, 77]]

def test_matmul_length_failure():
    with pytest.raises(ValueError):
        matmul([[1, 2]], [[1, 2]])