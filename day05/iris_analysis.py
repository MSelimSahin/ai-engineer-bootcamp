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
        print(class_name)
        for col, head in enumerate(header[:4]):
            values = [row[col] for row in rows if row[4] == class_name]
            m, s = statistics[class_name][head] = (mean(values), std(values))
            print(f"{head:>15}: {m:.2f} ± {s:.2f}")
