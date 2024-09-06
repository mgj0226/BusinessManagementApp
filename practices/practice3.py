"""
n is the number of towns
p is the number of towers
d is the distance a tower can cover
(xi, yi) is the coordinate of a town
((xi1 - xi2)^2 + (yi1 - yi2)^2)^0.5 is the distance between two towns
Pi1 is the number of people in town i1

We will be retrieving data from data.txt
The first line of the file contains n, p, and d
The next n lines contain xi-1(coordinate X for town i - 1), yi-1(coordinate Y for town i - 1), and Pi - 1(number of people in town i - 1)
Towns will be numbered from 1 to n
We will be building towers in towns one by one from the town that can cover the most towns
If two towns can cover the same number of towns, we will build the tower in the town with the smaller number
We will find which towns should we build towers in to cover all towns and the total number of people covered
e.g. 8 1 6 105 which means town 8, 1, 6 and 105 people
"""
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
    covered = {}
    for i in towns:
        for j in towns:
            if ((towns[i][0] - towns[j][0]) ** 2 + (towns[i][1] - towns[j][1]) ** 2) ** 0.5 <= d:
                covered[i] = covered.get(i, 0) + 1
    # for i in covered:
    #     print(i, covered[i])
    # build towers and tick off covered towns
    towers = []
    while len(towers) < p:
        max_covered = 0
        best_town = 0
        for i in covered:
            if covered[i] > max_covered:
                max_covered = covered[i]
                best_town = i
        towers.append(best_town)
        for i in towns:
            if ((towns[i][0] - towns[best_town][0]) ** 2 + (towns[i][1] - towns[best_town][1]) ** 2) ** 0.5 <= d:
                covered[i] = 0
    towers.sort()
    print(towers)
    total_people = 0
    for i in towers:
        total_people += towns[i][2]
    print(total_people)
    return
towers()