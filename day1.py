from typing import Counter, List


def part1(left_list: List[int], right_list: List[int]) -> int:
    left_list.sort()
    right_list.sort()

    res = 0

    for left, right in zip(left_list, right_list):
        res += abs(left - right)

    return res


def part2(left_list: List[int], right_list: List[int]) -> int:
    left_set = set(left_list)
    r_mp = Counter(right_list)
    res = 0
    for el in left_set:
        if el in r_mp:
            res += el * r_mp[el]

    return res


if __name__ == "__main__":
    input = open(0).read().splitlines()

    left_list = [int(row.split("   ")[0]) for row in input]
    right_list = [int(row.split("   ")[1]) for row in input]

    print(part2(left_list, right_list))
