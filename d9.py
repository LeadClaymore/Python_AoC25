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
    data = []
    with open("data/d9.txt", "r") as file:
        fileo = file.read().splitlines()

    for ee in fileo:
        if _debug:
            print(ee)
        a, b = ee.split(",")
        data.append([int(a), int(b)])
        if _debug:
            print(data[-1])

    largest = {}
    largest[0] = 0
    largest[1] = 1
    largest[2] = -1
    for ii in range(len(data)):
        ix, iy = data[ii][0], data[ii][1]
        for jj in range(ii + 1, len(data)):
            size = (abs(ix - data[jj][0]) + 1) * (abs(iy - data[jj][1]) + 1)
            if largest[2] < size:
                largest[0] = ii
                largest[1] = jj
                largest[2] = size

    print("ans: ", largest)


def parttwo():
    _ans = 0
    _debug = True
    fileo = []
    data = []
    with open("data/d9.txt", "r") as file:
        fileo = file.read().splitlines()

    for ee in fileo:
        if _debug:
            print(ee)
        a, b = ee.split(",")
        data.append([int(a), int(b)])
        if _debug:
            print(data[-1])
    
    largest = {}
    largest[0] = 0
    largest[1] = 1
    largest[2] = -1
    for ii in range(len(data)):
        ix, iy = data[ii][0], data[ii][1]
        for jj in range(ii + 1, len(data)):
            
            size = (abs(ix - data[jj][0]) + 1) * (abs(iy - data[jj][1]) + 1)
            if largest[2] < size:
                largest[0] = ii
                largest[1] = jj
                largest[2] = size

    print("ans: ", largest)
