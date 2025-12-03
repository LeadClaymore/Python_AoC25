import re


def partone():
    data = []
    ans = 0
    with open("data/d3.txt", "r") as file:
        data = file.read().splitlines()

    for ln in data:
        print(ln)
        highest = int(ln[0]) * 10 + int(ln[1])
        xx, yy = 0, 1
        cci = 0
        for cc in ln:
            ddi = 0
            for dd in ln:
                if cci < ddi and highest < int(cc) * 10 + int(dd):
                    highest, xx, yy = int(cc) * 10 + int(dd), cci, ddi
                ddi += 1
            cci += 1
        print(highest, xx, yy)
        ans += highest
    print(ans)


def parttwo():
    _debug = False
    data = []
    ans = 0
    with open("data/d3.txt", "r") as file:
        data = file.read().splitlines()

    for ln in data:
        if _debug:
            print(ln)
        inx = list(range(len(ln) - 12, len(ln)))
        pnt = -1
        if _debug:
            print(inx)
        for xx in range(12):
            for ii in range(pnt + 1, inx[xx] + 1):
                if int(ln[ii]) >= int(ln[inx[xx]]):
                    if ii > inx[xx] and int(ln[ii]) == int(ln[inx[xx]]):
                        continue

                    pnt = ii
                    inx[xx] = ii
        if _debug:
            print(inx)
        fn = ""
        for xx in inx:
            fn += ln[xx]
        ans += int(fn)
        if _debug:
            print(fn)
    print(ans)
