import os

def towers():
    data = []
    fname = "data.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fname)

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    data = [line.strip() for line in data]
    data = [(i) for i in data]

    n, p, d = data[0].split()
    n = int(n)
    p = int(p)
    d = int(d)
    towns = {}
    for i in range(1, n + 1):
        x, y, P = data[i].split()
        x = int(x)
        y = int(y)
        P = int(P)
        #name towns by number
        towns[i] = (x, y, P)
    # for i in towns:
    #     print(i, towns[i])
    class Town:
        def __init__(self, townNum):
            self.townNum = townNum
            self.covered = []
            self.totalCovered = 0
            self.totalPeopleCovered = 0
            self.isCovered = False

    town_objects = {i: Town(i) for i in towns}

    for i in towns:
        for j in towns:
            if ((towns[i][0] - towns[j][0]) ** 2 + (towns[i][1] - towns[j][1]) ** 2) ** 0.5 <= d:
                town_objects[i].totalCovered += 1
                town_objects[i].totalPeopleCovered += towns[j][2]
                town_objects[i].covered.append(j)

    # for i in town_objects:
    #     town = town_objects[i]
    #     print(f"Town {town.townNum}:")
    #     print(f"  Covered towns: {town.covered}")
    #     print(f"  Total towns covered: {town.totalCovered}")
    #     print(f"  Total people covered: {town.totalPeopleCovered}")
    #     print(f"  Is covered: {town.isCovered}")
    # build towers where most people are covered and tick off covered towns

    towers = []
    TotalPeopleCovered = 0
    while len(towers) < p:
        max_people_covered = 0
        best_town = 0
        for i in town_objects:
            town = town_objects[i]
            if town.totalPeopleCovered > max_people_covered and not town.isCovered:
                max_people_covered = town.totalPeopleCovered
                best_town = i
        # print(f"Best town: {best_town}")
        towers.append(best_town)
        TotalPeopleCovered += town_objects[best_town].totalPeopleCovered
        for j in town_objects[best_town].covered:
            town_objects[j].isCovered = True
            town_objects[j].totalPeopleCovered = 0
            town_objects[j].totalCovered = 0
            town_objects[j].covered = []
            # print(town_objects[j].townNum, town_objects[j].isCovered, town_objects[j].totalPeopleCovered, town_objects[j].totalCovered, town_objects[j].covered)

    #print towers and TotalPeopleCovered in x x x y format, no sorting needed
    print(" ".join([str(i) for i in towers]), TotalPeopleCovered)


    # for i in town_objects:
    #     print(f"Town {town.townNum}:")
    #     print(f"  Covered towns: {town.covered}")
    #     print(f"  Total towns covered: {town.totalCovered}")
    #     print(f"  Total people covered: {town.totalPeopleCovered}")
    #     print(f"  Is covered: {town.isCovered}")
    # print(towers)

towers()