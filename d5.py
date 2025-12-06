import re

# dirs visualized
# 0 1 2
# 7 x 3
# 6 5 4
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def partone():
    _debug = True
    data = []
    ans = 0
    with open("data/d5.txt", "r") as file:
        data = file.read().splitlines()

    range_pat = re.compile(r"^(\d+)-(\d+)$")
    single_pat = re.compile(r"^(\d+)$")

    ranges = []
    singles = []

    for ee in data:
        if _debug:
            print(ee)

        m = range_pat.match(ee)

        if m:
            a, b = map(int, m.groups())
            ranges.append((a, b))
        m = single_pat.match(ee)
        if m:
            singles.append(int(m.group(1)))

    for ee in singles:
        if _debug:
            print(ee)
        for rr in ranges:
            if ee >= rr[0] and ee <= rr[1]:
                ans += 1
                break
    print("ans: ", ans)


def parttwo():
    _debug = True
    data = []
    ans = 0
    with open("data/d5.txt", "r") as file:
        data = file.read().splitlines()

    range_pat = re.compile(r"^(\d+)-(\d+)$")
    single_pat = re.compile(r"^(\d+)$")

    ranges = []
    singles = []

    # _d_max = 0
    # _d_min = int(1e9)

    for ee in data:
        if _debug:
            print(ee)

        m = range_pat.match(ee)

        if m:
            a, b = map(int, m.groups())
            # if a > _d_max:
            #     _d_max = a
            # if b < _d_min:
            #     _d_min = b
            if a > b:
                print(f"\tinvalid range {a}-{b}")
            ranges.append((a, b))
        m = single_pat.match(ee)
        if m:
            singles.append(int(m.group(1)))

    # print(f"max: {_d_max}")
    # print(f"min: {_d_min}")

    prev_ranges = []

    for tee in ranges:
        ee0, ee1 = tee
        inval = False
        for pp in prev_ranges:
            # if the start of the curr range ee is within a previous range
            if pp[0] <= ee0 and pp[1] >= ee0:
                if pp[1] < ee1:
                    ee0 = pp[1] + 1
                else:
                    inval = True
                    break
            elif pp[0] <= ee1 and pp[1] >= ee1:
                if pp[0] > ee0:
                    ee1 = pp[0] - 1
                else:
                    # this should never happen bc the one above should have caught it
                    inval = True
                    break
            elif pp[0] >= ee0 and pp[1] <= ee1:
                ranges.append((pp[1], ee1))
                ee1 = pp[0] - 1

        if not inval:
            if _debug:
                print(f"range {ee0}-{ee1}")
            # idk if off by one
            ans += ee1 - ee0 + 1
            prev_ranges.append((ee0, ee1))

    print("ans: ", ans)
