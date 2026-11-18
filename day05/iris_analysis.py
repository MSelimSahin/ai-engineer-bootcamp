from day04.stats import mean, std
from day05.exercises import count_by

# a) Load data
def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        rows = []
        for line in f:
            if line == '':
                continue
            else:
                splitted_line = line.strip().split(",")
                floated_values = [float(splitted_line[i]) for i in range(4)]
                listed_str = splitted_line[4].split()
                row = floated_values + listed_str
                rows.append(row)

    return header, rows

# d) Split train/test data
def train_test_split(rows):
    test = []
    train = []
    [test.append(row) for idx, row in enumerate(rows) if idx % 5 == 0]
    [train.append(row) for idx, row in enumerate(rows) if idx % 5 != 0]
    return (train, test)

# e) nearest centroid classifier
# 1. train
def fit_centroids(train):
    centroid = {}
    species = []
    [species.append(row[4]) for row in train]
    pieces = count_by(species)
    for class_name in pieces.keys():
        centroid[class_name] = []
        for idx in range(len(train[0]) - 1):
            values = [row[idx] for row in train if row[4] == class_name]
            centroid[class_name].append(mean(values))
    return centroid

# e) nearest centroid classifier
# 2.1 euclid distance formula
def distance(a:list, b:list):
    if len(a) != len(b):
        raise ValueError(f"Length mismatch: {len(a)} vs {len(b)}")
    total = 0
    for idx in range(len(a)):
        total += (b[idx] - a[idx]) ** 2
    rooted_total = total ** 0.5
    return rooted_total

# e) nearest centroid classifier
# 2.2 prediction
def predict(features, centroids):
    min = float("inf")
    specie = ''
    for idx, centroid in enumerate(centroids.keys()):
        space = distance(features, centroids[centroid])
        if space < min:
            min = space
            specie = list(centroids.keys())[idx]
    return specie

if __name__ == "__main__":
    header, rows = load_csv("day05/iris.csv")

    # b) Species count
    species = []
    [species.append(row[4]) for row in rows]
    pieces = count_by(species)

    # c) statistics
    statistics = {}
    for class_name in pieces.keys():
        statistics[class_name] = {}
        # print(class_name)
        for col, head in enumerate(header[:4]):
            values = [row[col] for row in rows if row[4] == class_name]
            m, s = statistics[class_name][head] = (mean(values), std(values))
            # print(f"{head:>15}: {m:.2f} ± {s:.2f}")

    train, test = train_test_split(rows)
    centroids = fit_centroids(train)
    # print(centroids["setosa"])
    # print(predict([5.0, 3.4, 1.5, 0.2], centroids))

    # e) nearest centroid classifier
    # 3. Evaluation
    true_count = 0
    length = len(test)
    for row in test:
        prediction = predict(row[:-1], centroids)
        if row[-1] == prediction:
            true_count += 1
        else:
            print(f"It was {row[-1]}. But the model predicted {prediction}.")

    accuracy = (true_count / length) * 100
    print(f"The model's total accuracy is: {accuracy:.2f}%")

    assert distance([0, 0], [3, 4]) == 5.0
    assert distance([0, 0], [3, 4]) == 5.0                 # 2 dimensional
    assert distance([1, 2, 3, 4], [1, 2, 3, 4]) == 0       # same dot
    assert distance([0, 0, 0, 0], [1, 1, 1, 1]) == 2.0     # 4 dimensional
    assert predict([5.0, 3.4, 1.5, 0.2], centroids) == "setosa"
    assert predict([5.0, 3.4, 1.5, 0.2], centroids) == "setosa"
    assert predict([5.7, 2.8, 4.5, 1.3], centroids) == "versicolor"
    assert predict([6.5, 3.2, 5.1, 2.0], centroids) == "virginica"
    assert predict([4.97, 3.42, 1.45, 0.24], centroids) == "setosa"
    assert predict([6.2, 2.8, 4.9, 1.6], centroids) == "versicolor"   # 0.759 vs 0.788, kıl payı
    assert predict([6.3, 2.9, 5.0, 1.8], centroids) == "virginica"
    assert predict([7.0, 3.2, 4.7, 1.4], centroids) == "virginica"
    assert predict([0, 0, 0, 0], centroids) == "setosa"
    assert predict([100, 100, 100, 100], centroids) == "virginica"

    try:
        distance([1, 2], [1, 2, 3])
        assert False, "distance should have raised ValueError"
    except ValueError:
        pass