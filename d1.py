import re


def dayone():
    data = []
    with open("data/d1.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        print(ee)

    dcur = 50
    zcount = 0

    print(f"dc: {dcur}")

    for ln in data:
        pattern = re.compile(r"\b([A-Za-z])(\d+)\b")
        letter, number = "A", 0

        for match in pattern.finditer(ln):
            letter, number = match.group(1), int(match.group(2))  # unpack the groups
            print(f"letter={letter}, number={number!r}")

        
        if letter == "L":
            if (number % 100) > dcur:
                dcur = 100 + dcur - (number % 100)
            else:
                dcur = dcur - (number % 100)
        elif letter == "R":
            if (number % 100) + dcur > 99:
                dcur = (number % 100) + dcur - 100
            else:
                dcur = (number % 100) + dcur
        else:
            print(f"ERROR {letter}")
            break
        print(f"dc: {dcur}")
        if dcur == 0:
            print("\tReached 0")
            zcount += 1
        if dcur < 0:
            print(f"ERROR {dcur}")
            break
    print(f"zcount: {zcount}")
