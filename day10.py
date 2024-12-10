topo_map = list(
    map(lambda line: list(map(int, list(line))), open(0).read().splitlines())
)

start_pos = []
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
rows, cols = len(topo_map), len(topo_map[0])

for r, row in enumerate(topo_map):
    for c, cell in enumerate(row):
        if cell == 0:
            start_pos.append((r, c))


def count_paths(topo_map, sr, sc):
    rows, cols = len(topo_map), len(topo_map[0])
    # for part1  just switch this with a set
    nine_positions = []

    def dfs(r, c, path_height):
        # Out of bounds check
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        # Current cell height must strictly increase by 1
        if topo_map[r][c] != path_height + 1:
            return False

        # If we've reached height 9, mark it
        if topo_map[r][c] == 9:
            nine_positions.append((r, c))
            return True

        # Explore all four directions
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        found_trail = False
        for dx, dy in directions:
            new_r, new_c = r + dx, c + dy
            if dfs(new_r, new_c, topo_map[r][c]):
                found_trail = True

        return found_trail

    # Special approach for trailhead
    if topo_map[sr][sc] != 0:
        return 0

    # Try all directions from the trailhead
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_r, new_c = sr + dx, sc + dy
        dfs(new_r, new_c, 0)

    return len(nine_positions)


def part1():
    res = 0

    for sr, sc in start_pos:
        res += count_paths(topo_map, sr, sc)

    print("result", res)


part1()
