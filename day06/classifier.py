from day04.stats import mean
from day05.iris_analysis import load_csv, train_test_split, distance

class NearestCentroidClassifier:

    def __init__(self):
        self.centroids = None

    def fit(self, rows):
        self.centroids = {}
        species = [row[-1] for row in rows]
        pieces = set(species)
        for class_name in pieces:
            self.centroids[class_name] = []
            for idx in range(len(rows[0]) - 1):
                values = [row[idx] for row in rows if row[-1] == class_name]
                self.centroids[class_name].append(mean(values))
        return self

    def predict(self, features):
        if self.centroids is None:
            raise RuntimeError("Model is not fitted yet. Call fit() first.")
        best_distance = float("inf")
        specie = ''
        for name, center in self.centroids.items():
            space = distance(features, center)
            if space < best_distance:
                best_distance = space
                specie = name
        return specie

    def score(self, rows):
        true_count = 0
        length = len(rows)
        for row in rows:
            prediction = self.predict(row[:-1])
            if row[-1] == prediction:
                true_count += 1

        accuracy = (true_count / length)
        return accuracy

if __name__ == "__main__":
    n1 = NearestCentroidClassifier()
    header, rows = load_csv("day05/iris.csv")
    train, test = train_test_split(rows)
    try:
        n1.predict([5.0, 3.4, 1.5, 0.2])
    except RuntimeError as e:
        print(f"Error: {e}")

    try:
        load_csv("non-existing-file")
    except FileNotFoundError as e:
        print(f"Error: {e}")

    n1.fit(train)
    acc = NearestCentroidClassifier().fit(train).score(test)
    print(f"Test accuracy: {acc:.4f}")

    assert round(n1.score(test), 4) == 0.9667
    assert NearestCentroidClassifier().fit(train) is not None

    untrained = NearestCentroidClassifier()
    try:
        untrained.predict([5.0, 3.4, 1.5, 0.2])
        assert False, "predict should raise RuntimeError before fit"
    except RuntimeError:
        pass