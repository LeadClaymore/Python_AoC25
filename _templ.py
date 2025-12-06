# import re

# dirs visualized
# 0 1 2
# 7 x 3
# 6 5 4
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def partone():
    _debug = True
    data = []
    with open("data/t#.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        if _debug:
            print(ee)


def parttwo():
    _debug = True
    data = []
    with open("data/t#.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        if _debug:
            print(ee)
