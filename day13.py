from typing import DefaultDict, List
from sympy import symbols, Eq, solve
from collections import defaultdict
import re


def solve_claw(vars: DefaultDict[str, List[int]]):
    a, b = symbols("a b")
    eqs = []
    for values in vars.values():
        x, y, c = list(map(int, values))
        eqs.append(Eq(x * a + y * b, c))
    try:
        solution = solve(tuple(eqs), (a, b))
        a_sol, b_sol = solution.get(a), solution.get(b)
        if (
            a_sol
            and b_sol
            and a_sol % 1 == b_sol % 1 == 0
            and a_sol <= 100
            and b_sol <= 100
        ):
            return int(a_sol) * 3 + int(b_sol)
    except:
        return 0
    return 0


def part1():
    res = 0
    for line in open(0).read().split("\n\n"):
        vars = defaultdict(list)
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", line))
        vars["1"] = [ax, bx, px]
        vars["2"] = [ay, by, py]
        res += solve_claw(vars)
    print(res)


def solve_claw2(vars: DefaultDict[str, List[int]]):
    a, b = symbols("a b")
    eqs = []
    for values in vars.values():
        x, y, c = list(map(int, values))
        c += 10000000000000
        eqs.append(Eq(x * a + y * b, c))
        solution = solve(tuple(eqs), (a, b))
        a_sol, b_sol = solution.get(a), solution.get(b)
        if a_sol and b_sol and a_sol % 1 == b_sol % 1 == 0:
            return int(a_sol) * 3 + int(b_sol)

    return 0


"""
So turns out solving the equations manually by using solving for intersection of two lines makes it easy
Credits: @hyperneutrino
"""


def part2():
    res = 0
    for block in open(0).read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            res += int(3 * ca + cb)
    print(res)


part2()
