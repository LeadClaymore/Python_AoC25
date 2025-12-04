# import re


class Graph:
    mx = -1
    my = -1
    nodes = []

    def __init__(self, mx, my, data, _debug=False):
        self.mx = mx
        self.my = my
        for ii in range(mx):
            line = []
            for jj in range(my):
                if data[ii][jj] == "@":
                    line.append(Node(ii, jj, True))
                elif data[ii][jj] == ".":
                    line.append(Node(ii, jj, False))
                else:
                    print(f"ERROR at ({ii}, {jj})")
                    line.append(Node(ii, jj, False))
            self.nodes.append(line)
        # if _debug:
        #     print(self.nodes)

    def set_all_access(self):
        for ii in range(self.mx):
            for jj in range(self.my):
                self.set_access(ii, jj)

    def set_access(self, xx, yy):
        # dirs direction
        # 1 2 3
        # 0 x 4
        # 7 6 5
        dirs = [False] * 8
        yze = yy > 0
        yme = yy < self.my - 1
        xze = xx > 0
        xme = xx < self.mx - 1
        if yze:
            dirs[0] = self.nodes[xx][yy - 1].v

        if yze and xze:
            dirs[1] = self.nodes[xx - 1][yy - 1].v

        if xze:
            dirs[2] = self.nodes[xx - 1][yy].v

        if xze and yme:
            dirs[3] = self.nodes[xx - 1][yy + 1].v

        if yme:
            dirs[4] = self.nodes[xx][yy + 1].v

        if yme and xme:
            dirs[5] = self.nodes[xx + 1][yy + 1].v

        if xme:
            dirs[6] = self.nodes[xx + 1][yy].v

        if xme and yze:
            dirs[7] = self.nodes[xx + 1][yy - 1].v

        self.nodes[xx][yy].va = sum(dirs)

    def print(self):
        print("Value:")
        for ii in range(self.mx):
            line = ""
            for jj in range(self.my):
                if self.nodes[ii][jj].v:
                    line += "@"
                else:
                    line += "."
            print(line)

        print("\nValue in the Area:")
        for ii in range(self.mx):
            line = ""
            for jj in range(self.my):
                line += str(self.nodes[ii][jj].va)
            print(line)

    def get_ans(self):
        ans = 0
        for ii in range(self.mx):
            for jj in range(self.my):
                if self.nodes[ii][jj].v and self.nodes[ii][jj].va < 4:
                    ans += 1
        return ans

    def recalculate_adj(self, xx, yy):
        # dirs direction
        # 1 2 3
        # 0 x 4
        # 7 6 5
        yze = yy > 0
        yme = yy < self.my - 1
        xze = xx > 0
        xme = xx < self.mx - 1
        if yze:
            self.set_access(xx, yy - 1)

        if yze and xze:
            self.set_access(xx - 1, yy - 1)

        if xze:
            self.set_access(xx - 1, yy)

        if xze and yme:
            self.set_access(xx - 1, yy + 1)

        if yme:
            self.set_access(xx, yy + 1)

        if yme and xme:
            self.set_access(xx + 1, yy + 1)

        if xme:
            self.set_access(xx + 1, yy)

        if xme and yze:
            self.set_access(xx + 1, yy - 1)

        self.set_access(xx, yy)

    def get_p2_ans(self):
        ans = 0
        old_ans = -1
        while old_ans < ans:
            old_ans = ans
            for ii in range(self.mx):
                for jj in range(self.my):
                    if self.nodes[ii][jj].v and self.nodes[ii][jj].va < 4:
                        ans += 1
                        self.nodes[ii][jj].v = False
                        self.recalculate_adj(ii, jj)
        return ans


class Node:
    x = -1
    y = -1
    v = False
    va = 0

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.v = value

    def set_area(self, nva):
        self.va = nva


def partone():
    _debug = True
    data = []
    with open("data/d4.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        if _debug:
            print(ee)

    print("mx: ", len(data))
    print("my: ", len(data[0]))
    g = Graph(len(data), len(data[0]), data, _debug)
    g.set_all_access()
    if _debug:
        g.print()

    print("ans: ", g.get_ans())


def parttwo():
    _debug = True
    data = []
    with open("data/d4.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        if _debug:
            print(ee)

    print("mx: ", len(data))
    print("my: ", len(data[0]))
    g = Graph(len(data), len(data[0]), data, _debug)
    g.set_all_access()
    if _debug:
        g.print()

    print("ans: ", g.get_p2_ans())
