"""
Day 12: Garden Groups


so the idea here is to do a flood fill to find all the regions
flood fill => bfs

calc area and perimeter of each region and sum

part2 credit goes to hyperneutrino
this is where he told about the corner method that we can essentially count the corners for each region
which essentially represent a single fence between 2 corners

"""

from collections import deque

grid = list(map(list, open(0).read().splitlines()))

rows = len(grid)
cols = len(grid[0])


def directions(r, c):
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


def perimeter(region):
    p = 0
    for r, c in region:
        p += 4
        for nr, nc in directions(r, c):
            if (nr, nc) in region:
                p -= 1
    return p


def part1():
    regions = []
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited:
                continue
            visited.add((r, c))
            region = {(r, c)}
            q = deque([(r, c)])
            curr_char = grid[r][c]
            while q:
                cr, cc = q.popleft()
                for nr, nc in directions(cr, cc):
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] != curr_char:
                        continue
                    if (nr, nc) in region:
                        continue
                    region.add((nr, nc))
                    q.append((nr, nc))
            visited |= region
            regions.append(region)

    print(sum(len(region) * perimeter(region) for region in regions))


def corners(region):
    corners = 0
    possible_corners = set()
    for r, c in region:
        for nr, nc in [
            (r + 0.5, c + 0.5),
            (r - 0.5, c + 0.5),
            (r + 0.5, c - 0.5),
            (r - 0.5, c - 0.5),
        ]:
            possible_corners.add((nr, nc))

    for r, c in possible_corners:
        config = [
            (sr, sc) in region
            for sr, sc in [
                (r + 0.5, c + 0.5),
                (r - 0.5, c + 0.5),
                (r + 0.5, c - 0.5),
                (r - 0.5, c - 0.5),
            ]
        ]
        no_of_corners = sum(config)
        if no_of_corners == 1:
            corners += 1
        elif no_of_corners == 2:
            if config == [True, False, False, True] or config == [
                False,
                True,
                True,
                False,
            ]:
                corners += 2
        elif no_of_corners == 3:
            corners += 1
    return corners


def part2():
    regions = []
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if (r, c) in visited:
                continue
            visited.add((r, c))
            region = {(r, c)}
            q = deque([(r, c)])
            curr_char = grid[r][c]
            while q:
                cr, cc = q.popleft()
                for nr, nc in directions(cr, cc):
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] != curr_char:
                        continue
                    if (nr, nc) in region:
                        continue
                    region.add((nr, nc))
                    q.append((nr, nc))
            visited |= region
            regions.append(region)

    print(sum(len(region) * corners(region) for region in regions))


part2()
