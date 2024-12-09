"""
Example 1:

4,5 - 6, 6

diff => 2, 1 -> 2 antinodes -> 2, 4 and 8, 7

gather coords for each freq

for all the coords of same freq
-> pair each point with another point
=> calc dist between them -> r2 - r1, c2 - c1
-> subtract from first coords in pair and add to second coords in pair -> 2 * r1 - r2, 2 * c1 - c2 && 2 * r2 - r1, 2 * c2 - c1
=> filter antinodes which are outside of grid

"""

grid = open(0).read().splitlines()


def part1():
    mp = {}
    antinodes = set()
    rows = len(grid)
    cols = len(grid[0])

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == ".":
                continue
            if cell not in mp:
                mp[cell] = []
            mp[cell].append((r, c))

    for coords in mp.values():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                r1, c1 = coords[i]
                r2, c2 = coords[j]
                antinodes.add((2 * r1 - r2, 2 * c1 - c2))
                antinodes.add((2 * r2 - r1, 2 * c2 - c1))

    print(len([(r, c) for r, c in antinodes if 0 <= r < rows and 0 <= c < cols]))


def part2():
    mp = {}
    antinodes = set()
    rows = len(grid)
    cols = len(grid[0])

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == ".":
                continue
            if cell not in mp:
                mp[cell] = []
            mp[cell].append((r, c))

    for coords in mp.values():
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i == j:
                    continue
                r1, c1 = coords[i]
                r2, c2 = coords[j]
                dr, dc = r2 - r1, c2 - c1
                r, c = r1, c1
                while 0 <= r < rows and 0 <= c < cols:
                    antinodes.add((r, c))
                    r += dr
                    c += dc

    print(len(antinodes))


part2()
