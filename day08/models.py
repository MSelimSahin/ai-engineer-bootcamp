from day05.iris_analysis import load_csv, train_test_split, distance
from day04.stats import mean
from day08.exercises import majority_vote
import json

class BaseClassifier:
    
    def fit(self, rows):
        raise NotImplementedError
    
    def predict(self, features):
        raise NotImplementedError
    
    def score(self, rows):
        true_count = 0
        length = len(rows)
        for row in rows:
            prediction = self.predict(row[:-1])
            if row[-1] == prediction:
                true_count += 1

        accuracy = (true_count / length)
        return accuracy

class NearestCentroidClassifier(BaseClassifier):

    def __init__(self):
        self.centroids = None

    def __repr__(self):
        return f"NearestCentroidClassifier"

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

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.centroids, f)

    def load(self, path):
        with open(path, "r") as f:
            self.centroids = json.load(f)
            return self

class KNNClassifier(BaseClassifier):

    def __init__(self, k=3):
        if not isinstance(k, int) or k <= 0:
            raise ValueError(f"k must be a positive integer, got {k}")
        self.k = k
        self.rows = None

    def __repr__(self):
        return f"KNNClassifier(k={self.k})"

    def fit(self, rows):
        self.rows = rows
        return self

    def predict(self, features):
        if self.rows is None:
            raise RuntimeError("Model is not fitted yet. Call fit() first.")
        nearest = sorted(self.rows, key=lambda row: distance(row[:-1], features))[:self.k]
        labels = [row[-1] for row in nearest]
        return majority_vote(labels)


if __name__ == "__main__":

    knn = KNNClassifier()
    header, rows = load_csv("day05/iris.csv")
    train, test = train_test_split(rows)
    fitted_knn = knn.fit(train)
    print(fitted_knn.predict([5.0, 3.4, 1.5, 0.2]))

    model = NearestCentroidClassifier().fit(train)
    model.save("model.json")

    loaded = NearestCentroidClassifier().load("model.json")
    assert loaded.predict([5.0, 3.4, 1.5, 0.2]) == model.predict([5.0, 3.4, 1.5, 0.2])