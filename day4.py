from typing import List, Tuple

matching_word = list("XMAS")


def is_safe(nr: int, nc: int, r: int, c: int, i: int) -> bool:
    return 0 <= r < nr and 0 <= c < nc and grid[r][c] == matching_word[i]


def part1(grid: List[List[str]]):
    start_pos = set(
        [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == "X"]
    )

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    res = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in start_pos:
                for dr, dc in directions:
                    for i in range(1, len(matching_word)):
                        if is_safe(len(grid), len(grid[0]), r + i * dr, c + i * dc, i):
                            continue
                        else:
                            break
                    else:
                        res += 1

    return res


directions2 = [((-1, -1), (1, 1)), ((1, -1), (-1, 1))]


def is_safe2(
    nr: int,
    nc: int,
    r: int,
    c: int,
) -> bool:
    return 0 <= r < nr and 0 <= c < nc


def checkX(nr: int, nc: int, r: int, c: int, grid):
    for (dr1, dc1), (dr2, dc2) in directions2:
        if (
            is_safe2(nr, nc, r + dr1, c + dc1)
            and is_safe2(nr, nc, r + dr2, c + dc2)
            and {"M", "S"}
            == {
                grid[r + dr1][c + dc1],
                grid[r + dr2][c + dc2],
            }
        ):
            continue
        else:
            return False
    else:
        return True


def part2(grid: List[List[str]]):
    start_pos = set(
        [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == "A"]
    )

    res = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in start_pos:
                if checkX(len(grid), len(grid[0]), r, c, grid):
                    res += 1

    return res


if __name__ == "__main__":
    input = open(0).read().strip().splitlines()
    grid = [list(c) for c in input]

    # res = part1(grid)
    res2 = part2(grid)

    print(res2)
