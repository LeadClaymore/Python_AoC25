# import re

# dirs visualized
# 0 1 2
# 7 x 3
# 6 5 4
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


class node:
    x: int
    y: int

    def __init__(self, tx, ty) -> None:
        self.x = tx
        self.y = ty

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


def partone():
    _debug = True
    data = []
    ans = 0
    with open("data/d7.txt", "r") as file:
        pre_data = file.read().splitlines()
        for ii in pre_data:
            line = []
            for jj in ii:
                line.append(jj)
            data.append(line)

    for ee in data:
        if _debug:
            print(ee)

    for ii in range(len(data) - 1):
        for jj in range(len(data[ii])):
            if data[ii][jj] == "S":
                if data[ii + 1][jj] == "^":
                    ans += 1
                    data[ii + 1][jj + 1] = "S"
                    data[ii + 1][jj - 1] = "S"
                else:
                    data[ii + 1][jj] = "S"

    print(data[-1])
    # print("ans: ", data[-1].count("S"))
    print("ans: ", ans)


def parttwo():
    _debug = False
    data = []
    ans = 0
    with open("data/d7.txt", "r") as file:
        pre_data = file.read().splitlines()
        for ii in pre_data:
            line = []
            for jj in ii:
                line.append(jj)
            data.append(line)

    for ee in data:
        if _debug:
            print(ee)

    poses: list[node] = []
    for ii in range(len(data[0])):
        if data[0][ii] == "S":
            poses.append(node(0, ii))
            break
    if not poses:
        print("ERROR: start is null")
        return

    check = 0
    while poses:
        # check -= 1
        # if check < 0:
        #     print("Error inf loop")
        #     return

        nn = poses.pop(0)
        if nn.x >= check:
            print(f"check: {nn.x}")
            check = nn.x + 1
        if nn.x == len(data) - 1:
            ans += 1
        elif data[nn.x + 1][nn.y] == "^":
            poses.append(node(nn.x + 1, nn.y + 1))
            nn.x = nn.x + 1
            nn.y = nn.y - 1
            poses.append(nn)
        else:
            nn.x = nn.x + 1
            poses.append(nn)

        if _debug:
            print(*poses, sep=" ")

    print(data[-1])
    # print("ans: ", data[-1].count("S"))
    print("ans: ", ans)


def parttwotrytwo():
    _debug = False
    data = []
    ans = 0
    with open("data/d7.txt", "r") as file:
        pre_data = file.read().splitlines()
        for ii in pre_data:
            line = []
            for jj in ii:
                line.append(jj)
            data.append(line)

    for ee in data:
        if _debug:
            print(ee)

    map: dict[int, int] = {}

    for ii in range(len(data[0])):
        if data[0][ii] == "S":
            map[ii] = 1
            break
    if not map:
        print("ERROR: start is null")
        return

    for ii in range(len(data)):
        for jj in range(len(data[ii])):
            if data[ii][jj] == "^":
                if map.__contains__(jj - 1):
                    map[jj - 1] += map[jj]
                else:
                    map[jj - 1] = map[jj]
                if map.__contains__(jj + 1):
                    map[jj + 1] += map[jj]
                else:
                    map[jj + 1] = map[jj]
                map[jj] = 0

    for _key, val in map.items():
        ans += val
    print("ans: ", ans)
