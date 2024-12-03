from typing import List


def part1(rows: List[List[int]]) -> int:
    res = 0
    for row in rows:
        if isSafeDistance(row) and checkMontonic(row):
            res += 1

    return res


def part2(rows: List[List[int]]):
    res = 0
    for row in rows:
        res = part2Process(res, row)

    return res


def part2Process(res: int, row: List[int]):
    if isSafeDistance(row) and checkMontonic(row):
        return res + 1

    for i in range(0, len(row)):
        new_row = row.copy()
        del new_row[i]
        if isSafeDistance(new_row) and checkMontonic(new_row):
            return res + 1

    return res


def isSafeDistance(arr: List[int]):
    return all(abs(arr[i] - arr[i - 1]) < 4 for i in range(1, len(arr)))


def checkMontonic(arr: List[int]):
    inc = all(el > arr[i - 1] for i, el in enumerate(arr) if i > 0)
    dec = all(el < arr[i - 1] for i, el in enumerate(arr) if i > 0)

    return inc or dec


if __name__ == "__main__":
    input = open(0).read().splitlines()

    rows = list(map(lambda x: list(map(int, x.split())), input))

    print(part1(rows))
    print(part2(rows))
