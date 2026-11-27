from day05.iris_analysis import distance
from day05.exercises import count_by

# a)
points = [("Hans", 72), ("Jack", 91), ("Tom", 85)]
points_sorted = sorted(points, key=lambda pair: pair[1], reverse=True)

# b) 
def closest_to_origin(points):
    return min(points, key=lambda p: distance(p, [0] * len(p)))

# c)
def majority_vote(labels):
    if not labels:
        raise ValueError("Labels must not be empty.")
    total = count_by(labels)
    maximum = max(total, key=lambda p: total[p])
    return maximum

if __name__ == "__main__":
    print(points_sorted)