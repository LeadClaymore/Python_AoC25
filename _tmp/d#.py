# import re

# dirs visualized
# 0 1 2
# 7 x 3
# 6 5 4
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def partone():
    _ans = 0
    _debug = True
    fileo = []
    with open("data/t#.txt", "r") as file:
        fileo = file.read().splitlines()

    for ee in fileo:
        if _debug:
            print(ee)


def parttwo():
    _ans = 0
    _debug = True
    fileo = []
    with open("data/t#.txt", "r") as file:
        fileo = file.read().splitlines()

    for ee in fileo:
        if _debug:
            print(ee)
