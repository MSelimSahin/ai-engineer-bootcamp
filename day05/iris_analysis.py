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

if __name__ == "__main__":
    header, rows = load_csv("day05/iris.csv")
    print(len(rows))

    # b) Species count
    species = []
    [species.append(row[4]) for row in rows]
    count_by(species)

    # c) statistics
    