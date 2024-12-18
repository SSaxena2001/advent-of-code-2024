from collections import deque


def part1():
    s = 70
    n = 1024

    grid = [[0 for _ in range(s + 1)] for _ in range(s + 1)]

    corrupted = [list(map(int, line.split(","))) for line in open(0)]

    for x, y in corrupted[:n]:
        grid[x][y] = -1

    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        r, c, d = q.popleft()
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if nr < 0 or nc < 0 or nr > s or nc > s:
                continue
            if grid[nr][nc] == -1:
                continue
            if (nr, nc) in seen:
                continue
            if nr == nc == s:
                print(d + 1)
                exit(0)
            seen.add((nr, nc))
            q.append((nr, nc, d + 1))


part1()
