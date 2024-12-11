"""
Day 11: Plutonian Pebbles

list of the stones and then perform the operation

125 17

After 1 blink:
253000 1 7

After 2 blinks:
253 0 2024 14168

After 3 blinks:
512072 1 20 24 28676032

After 4 blinks:
512 72 2024 2 0 2 4 2867 6032

After 5 blinks:
1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32

After 6 blinks:
2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

"""

from typing import List
from functools import cache
import sys

sys.setrecursionlimit(10**6)


def operation(stone: int):
    if stone == 0:
        return 1
    if len(str(stone)) % 2 == 0:
        ss = str(stone)
        mid = len(ss) // 2
        return [int(ss[:mid]), int(ss[mid:])]
    else:
        return stone * 2024


def part1():
    stones = list(map(int, input().split()))
    res: List[int] = []
    temp = stones.copy()
    count = 0
    while count < 25:
        res.clear()
        for stone in temp:
            result = operation(stone)
            if isinstance(result, int):
                res.append(result)
            else:
                res += result
        temp = res.copy()
        count += 1

    print(len(res))


@cache
def counting(stone, count):
    if count == 0:
        return 1
    if stone == 0:
        return counting(1, count - 1)
    if len(str(stone)) % 2 == 0:
        ss = str(stone)
        mid = len(ss) // 2
        return counting(int(ss[:mid]), count - 1) + counting(int(ss[mid:]), count - 1)
    return counting(stone * 2024, count - 1)


def part2():
    stones = list(map(int, input().split()))

    print(sum(counting(stone, 75) for stone in stones))


part2()
