import re


def partone():
    _debug = False
    data = []
    ans = 0

    with open("data/d2.txt", "r") as file:
        data = file.read().split(",")

    for ee in data:
        print(ee)

    for rng in data:
        pattern = re.compile(r"\b(\d+)-(\d+)\b")
        lhs, rhs = 0, 0

        for match in pattern.finditer(rng):
            lhs, rhs = int(match.group(1)), int(match.group(2))  # unpack the groups
            if _debug:
                print(f"lhs={lhs!r}, rhs={rhs!r}")

            for ii in range(lhs, rhs + 1):
                digits = len(str(ii))
                # hdp: int = int(10 ** (digits / 2))
                # if _debug:
                #     th = int(ii / hdp)
                #     bh = ii % hdp
                #     print(f"hdp={hdp}, th={th}, bh={bh}")
                if digits % 2 != 0:
                    continue
                hdp: int = int(10 ** (digits / 2))
                if ii % hdp == int(ii / hdp):
                    ans += ii
    print(ans)


def parttwo():
    _debug = False
    data = []
    ans = 0
    # lfd = 0

    with open("data/d2.txt", "r") as file:
        data = file.read().split(",")

    for ee in data:
        print(ee)

    for rng in data:
        pattern = re.compile(r"\b(\d+)-(\d+)\b")
        lhs, rhs = 0, 0

        for match in pattern.finditer(rng):
            lhs, rhs = int(match.group(1)), int(match.group(2))  # unpack the groups
            if _debug:
                print(f"lhs={lhs!r}, rhs={rhs!r}")

            for ii in range(lhs, rhs + 1):
                strii = str(ii)
                digits = len(str(ii))

                for dd in range(2, digits + 1):
                    if digits % dd != 0:
                        continue
                    flvs = False
                    slc = int(digits / dd)
                    cmp = strii[0:slc]
                    for jj in range(slc, digits, slc):
                        if strii[jj : jj + slc] == cmp:
                            if jj + slc == digits:
                                ans += ii
                                flvs = True
                                if _debug:
                                    print(f"\t{ii} ->{cmp}")
                        else:
                            break
                    if flvs:
                        break
    print(ans)
    # print(lfd)
