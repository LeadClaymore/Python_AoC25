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

    with open("data/d8.txt", "r") as file:
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

    for _count in range(999):
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
        if min_dist == inf:
            print("error: ran out of connections")
            return
        to_update = jbs[lhs].cmb(jbs[rhs])
        for uu in to_update:
            jbs[uu].cmb(jbs[lhs])

        if _debug:
            print(f"{_count}: {jbs[lhs].x} <-> {jbs[rhs].x}")

    if _debug:
        for ee in jbs.values():
            print(ee)

    ans_sets: list[set[int]] = []
    for ee in jbs:
        in_set = False
        for aa in ans_sets:
            if aa == jbs[ee].c:
                in_set = True
        if not in_set:
            ans_sets.append(jbs[ee].c)

    while len(ans_sets) > 3:
        smallest_set = 0
        for ii in range(1, len(ans_sets)):
            if len(ans_sets[ii]) < len(ans_sets[smallest_set]):
                smallest_set = ii
        ans_sets.pop(smallest_set)

    ans = 1
    for ee in ans_sets:
        print(ans, "\t", ee, len(ee))
        ans *= len(ee)

    print(ans)


class con:
    dist: float
    lhs: int
    rhs: int

    def __init__(self, ndist: float, nlhs: int, nrhs: int) -> None:
        self.dist = ndist
        self.lhs = nlhs
        self.rhs = nrhs

    def __str__(self) -> str:
        return f"<{self.lhs} -{self.dist}- {self.rhs}>"


def partonetrytwo():
    _ans = 0
    _debug = False
    data = []
    jbs: dict[int, jb] = {}
    circuts: list[list[int]] = []
    conn: list[con] = []

    with open("data/d8.txt", "r") as file:
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

    used = set()
    for ee in jbs.values():
        for ff in jbs.values():
            if ee.id == ff.id or used.__contains__(ff):
                continue
            tdist = ee.dist(ff)
            # print(f"{ee.id}, {ff.id}, {tdist}")
            conn.append(con(tdist, ee.id, ff.id))
        used.add(ee)
    # this sorts the connections list
    # for cc in conn:
    #     print(cc)
    conn.sort(key=lambda c: c.dist)
    # if _debug:
    #     for cc in conn:
    #         print(cc)

    for ii in jbs.keys():
        circuts.append([ii])

    for cc in range(1000):
        if _debug:
            print(f"conn {conn[cc]}")
        ind = (conn[cc].lhs, conn[cc].rhs)
        con_ind = [-1, -1]
        for ii in range(2):
            for ee in range(len(circuts)):
                if circuts[ee].__contains__(ind[ii]):
                    con_ind[ii] = ee
                    break

        if _debug:
            print(con_ind, len(circuts))
        if con_ind[0] == -1 or con_ind[1] == -1:
            print(f"ERROR: could not find {ind[0]} or {ind[1]}")
            return
        elif con_ind[0] == con_ind[1]:
            continue
        temp_list = []
        if con_ind[0] > con_ind[1]:
            temp_list.extend(circuts.pop(con_ind[0]))
            temp_list.extend(circuts.pop(con_ind[1]))
        else:
            temp_list.extend(circuts.pop(con_ind[1]))
            temp_list.extend(circuts.pop(con_ind[0]))
        circuts.append(temp_list)
        if _debug:
            print(f"{cc}, new combined list {temp_list}")

    circuts.sort(key=lambda lst: -len(lst))
    ans = len(circuts[0]) * len(circuts[1]) * len(circuts[2])
    print("ans: ", ans)
    return


def parttwo():
    _ans = 0
    _debug = False
    data = []
    jbs: dict[int, jb] = {}
    circuts: list[list[int]] = []
    conn: list[con] = []

    with open("data/d8.txt", "r") as file:
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

    used = set()
    for ee in jbs.values():
        for ff in jbs.values():
            if ee.id == ff.id or used.__contains__(ff):
                continue
            tdist = ee.dist(ff)
            # print(f"{ee.id}, {ff.id}, {tdist}")
            conn.append(con(tdist, ee.id, ff.id))
        used.add(ee)
    # this sorts the connections list
    # for cc in conn:
    #     print(cc)
    conn.sort(key=lambda c: c.dist)
    # if _debug:
    #     for cc in conn:
    #         print(cc)

    for ii in jbs.keys():
        circuts.append([ii])

    # for ee in conn:
    #     print(ee)
    # return

    last_con = -1
    for cc in range(len(conn)):
        if _debug:
            print(f"conn {conn[cc]}")
        ind = (conn[cc].lhs, conn[cc].rhs)
        con_ind = [-1, -1]
        for ii in range(2):
            for ee in range(len(circuts)):
                if circuts[ee].__contains__(ind[ii]):
                    con_ind[ii] = ee
                    break

        if _debug:
            print(con_ind, len(circuts))
        if con_ind[0] == -1 or con_ind[1] == -1:
            print(f"ERROR: could not find {ind[0]} or {ind[1]}")
            return
        elif con_ind[0] == con_ind[1]:
            continue

        last_con = cc
        temp_list = []
        if con_ind[0] > con_ind[1]:
            temp_list.extend(circuts.pop(con_ind[0]))
            temp_list.extend(circuts.pop(con_ind[1]))
        else:
            temp_list.extend(circuts.pop(con_ind[1]))
            temp_list.extend(circuts.pop(con_ind[0]))
        circuts.append(temp_list)
        if _debug:
            print(f"{cc}, new combined list {temp_list}")

    _ans = jbs[conn[last_con].lhs].x * jbs[conn[last_con].rhs].x
    print(f"ans: {_ans}, {conn[last_con]}")
    return
