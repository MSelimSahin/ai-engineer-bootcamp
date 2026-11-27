import random

from day05.iris_analysis import load_csv

def batches(rows, batch_size, shuffle=False, seed=None):
    if not isinstance(batch_size, int) or batch_size <= 0:
        raise ValueError("batch size must be a positive integer")
    if seed is None:
        if shuffle:
            copy_rows = rows[:]
            random.shuffle(copy_rows)
            for i in range(0, len(rows), batch_size):
                yield copy_rows[i:i + batch_size]
        else:
            for i in range(0, len(rows), batch_size):
                yield rows[i:i + batch_size]
    else:
        if not shuffle:
            raise ValueError("shuffle must not be False when seed is given.")
        else:
            copy_rows = rows[:]
            random.Random(seed).shuffle(copy_rows)
            for i in range(0, len(rows), batch_size):
                yield copy_rows[i:i + batch_size]

if __name__ == "__main__":
    header, rows = load_csv("day05/iris.csv")
    print([len(b) for b in batches(rows, 32, True, 1453)])