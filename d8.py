import re
from ast import BoolOp
from math import inf, sqrt

# dirs visualized
# 0 1 2
# 7 x 3
# 6 5 4
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


class jb:
    id: int
    x: int
    y: int
    z: int
    c: set[int]

    def __init__(self, nid, nx, ny, nz) -> None:
        self.id = nid
        self.x = nx
        self.y = ny
        self.z = nz
        self.c = set({nid})

    def __str__(self) -> str:
        clist = list(self.c)
        return f"<id{self.id} x{self.x} y{self.y} z{self.z} c{clist.__str__()}>"

    def dist(self, ojb: jb) -> float:
        if self.id == ojb.id:
            print(f"{self.id} tried to get the dist of self")
            return inf
        return sqrt(
            (self.x - ojb.x) ** 2 + (self.y - ojb.y) ** 2 + (self.z - ojb.z) ** 2
        )

    def cmb(self, ojb: jb) -> set[int]:
        self.c.update(ojb.c)
        ojb.c.update(self.c)
        # ojb.c.add(self.id)
        # self.c.add(ojb.id)
        return self.c

    def add_to_connection(self, tu: set[int]) -> None:
        self.c.update(tu)

    def is_con(self, oid: int) -> bool:
        return self.c.__contains__(oid)


def partone():
    _ans = 0
    _debug = True
    data = []
    jbs: dict[int, jb] = {}

    with open("data/t8.txt", "r") as file:
        data = file.read().splitlines()

    cnt = 0
    for ee in data:
        cnt += 1

        pat = re.compile(r"^(\d+),(\d+),(\d+)$")
        m = pat.match(ee)

        if m:
            a, b, c = map(int, m.groups())
            if _debug:
                print(f"a:{a},b:{b},c:{c}")
            jbs[cnt] = jb(cnt, a, b, c)
        else:
            print("ERROR")
            return

    for _count in range(9):
        min_dist = inf
        lhs, rhs = (-1, -1)
        for ee in jbs.values():
            # if _debug:
            #     print(ee)
            for ff in jbs.values():
                if ee.id == ff.id or ee.is_con(ff.id):
                    continue
                temp = ee.dist(ff)
                if temp < min_dist:
                    lhs, rhs = (ee.id, ff.id)
                    min_dist = temp

        to_update = jbs[lhs].cmb(jbs[rhs])
        for uu in to_update:
            jbs[uu].cmb(jbs[lhs])

        if _debug:
            print(f"{_count}: {jbs[lhs].x} <-> {jbs[rhs].x}")

    if _debug:
        for ee in jbs.values():
            print(ee)


def parttwo():
    _ans = 0
    _debug = True
    data = []
    with open("data/t8.txt", "r") as file:
        data = file.read().splitlines()
