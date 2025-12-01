# test file


def test_read_file():
    data = []
    with open("data/test.txt", "r") as file:
        data = file.read().splitlines()

    for ee in data:
        print(ee)
