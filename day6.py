grid = list(map(list, open(0).read().strip().splitlines()))

rows = len(grid)
cols = len(grid[0])


def get_start_pos():
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "^":
                return (r, c)

    return (0, 0)


def part1():
    r, c = get_start_pos()
    dr = -1
    dc = 0

    seen = set()

    while True:
        seen.add((r, c))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            break
        if grid[r + dr][c + dc] == "#":
            dr, dc = dc, -dr
        else:
            r += dr
            c += dc

    print(len(seen))


def in_loop(grid, r, c):
    dr = -1
    dc = 0

    seen = set()

    while True:
        seen.add((r, c, dr, dc))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            return False
        if grid[r + dr][c + dc] == "#":
            dr, dc = dc, -dr
        else:
            r += dr
            c += dc
        if (r, c, dr, dc) in seen:
            return True


def part2():
    r, c = get_start_pos()
    total = 0

    # Brute forcing each point to see if it's in a loop -> TODO: optimize, find a better way for this
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] != ".":
                continue
            grid[x][y] = "#"
            if in_loop(grid, r, c):
                total += 1
            grid[x][y] = "."

    # using part1 as tracker

    print(total)


part2()
