from day04.ml_toolkit import dot
# a) flatten a list
def flatten(nested: list) -> list:
    # Python 3.15+ only (PEP 798)
    # flattened = [*value for value in nested]
    return [y for x in nested for y in x]

# b) transpose a matrix
def transpose(matrix):
    if len(matrix) == 0:
        return []
    return [[x[idx] for x in matrix] for idx in range(len(matrix[0]))]

# c) matris multiply
def matmul(A, B):
    if len(A[0]) == len(B):
        transposed_b = transpose(B)
        return [[dot(row, col) for col in transposed_b] for row in A]
    raise ValueError(f"Length mismatch: {len(A[0])} vs {len(B)}")

# d) count each element occuring in the list
def count_by(items: list) -> dict:
    total_times = {}
    for item in items:
        total_times[item] = total_times.get(item, 0) + 1
    return total_times

if __name__ == "__main__":
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert count_by(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert matmul([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]) == [[14, 32], [32, 77]]
    assert transpose([]) == []
    assert flatten([[1, 1], [2, 1]]) == [1, 1, 2, 1]

    try:
        matmul([[1, 2]], [[1, 2]])
        assert False, "matmul should have raised ValueError"
    except ValueError:
        pass