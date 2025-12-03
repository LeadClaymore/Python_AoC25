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
    data = []
    with open("data/a1.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        print(ee)
