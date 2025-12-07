# import re


def partone():
    _debug = True
    data = []
    nums = []
    ops = []
    ans = 0
    with open("data/d6.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        line = ee.strip().split(" ")
        r_line = []

        if _debug:
            print(line)

        for ii in range(len(line)):
            if line[ii] != "":
                if line[ii].isnumeric():
                    r_line.append(int(line[ii]))
                else:
                    r_line.append(line[ii])

        if _debug:
            print(r_line)

        if line[0].isnumeric():
            nums.append(r_line)
        else:
            ops = r_line

    for oo in range(len(ops)):
        num = 0
        if ops[oo] == "*":
            num = nums[0][oo]
            for ii in range(1, len(nums)):
                num *= nums[ii][oo]
            print(f"line {oo}, *, {num}")
        elif ops[oo] == "+":
            num = nums[0][oo]
            for ii in range(1, len(nums)):
                num += nums[ii][oo]
            print(f"line {oo}, +, {num}")
        else:
            print(f"ERROR op is: ", ops[oo])
            break
        ans += num
    print("ans: ", ans)


# TODO spacing matters
def parttwo():
    _debug = True
    data = []
    pplines: list[str] = []

    nums = []
    ops = []
    spaces = []
    ans = 0
    tempnums: list[list[str]] = []

    with open("data/d6.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        line = str(ee)
        # tempnums.append([])
        if _debug:
            print(line)
        pplines.append(line)

    temp: str = pplines[-1]
    t_spaces: int = 1
    for ii in range(1, len(temp)):
        if temp[ii] == " ":
            t_spaces += 1
        elif temp[ii] == "+" or temp[ii] == "*":
            to_send: list[str] = []
            for jj in range(len(pplines) - 1):
                to_send.append(pplines[jj][ii - t_spaces : ii])
            ans += cep_math(temp[ii - t_spaces], to_send, _debug)
            t_spaces = 1
        else:
            print(f"Error temp[{ii}] = ", temp[ii])
            return
    last_to_send: list[str] = []
    for jj in range(len(pplines) - 1):
        last_to_send.append(pplines[jj][len(temp) - t_spaces : len(pplines[jj])])
    ans += cep_math(temp[len(temp) - t_spaces], last_to_send, _debug)
    print("ans: ", ans)


def cep_math(op: str, nums: list[str], _debug=False) -> int:
    ret = 0
    temp_num = 0

    if _debug:
        print("op = ", op)
        for nn in nums:
            print(f"\t|{nn}|")

    for ii in range(len(nums[0])):
        for jj in nums:
            if jj[ii] != " ":
                temp_num = temp_num * 10 + int(jj[ii])

        if temp_num == 0:
            continue

        if _debug:
            print(temp_num)

        if op == "*":
            if ret == 0:
                ret = temp_num
            else:
                ret = ret * temp_num
            temp_num = 0
        elif op == "+":
            ret += temp_num
            temp_num = 0
        else:
            print("ERROR op = ", op)
            return -1

    if _debug:
        print("ret: ", ret)
    return ret
