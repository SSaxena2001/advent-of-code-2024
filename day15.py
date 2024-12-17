warehouse, movements = open(0).read().strip().split("\n\n")
warehouse = warehouse.splitlines()

R = len(warehouse)
C = len(warehouse[0])

warehouse = [[warehouse[r][c] for c in range(C)] for r in range(R)]

"""
@ -> robot,
O -> box,
# -> wall

we need to find position of all boxes after robot is done

simulating seems more work here but I'm trying cause why not

and it works just fine
"""

box = "O"
wall = "#"
robot = "@"
directions = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}

start_pos = (0, 0)
for r in range(R):
    for c in range(C):
        if warehouse[r][c] == robot:
            start_pos = (r, c)
            warehouse[r][c] = "."
            break

r, c = start_pos

for move in movements:
    if move == "\n":
        continue
    dr, dc = directions[move]
    print(r, c, move)
    rr, cc = r + dr, c + dc
    if warehouse[rr][cc] == wall:
        continue
    elif warehouse[rr][cc] == ".":
        r, c = rr, cc
    elif warehouse[rr][cc] == box:
        while warehouse[rr][cc] == box:
            rr += dr
            cc += dc
        if warehouse[rr][cc] == wall:
            continue
        elif warehouse[rr][cc] == ".":
            while (rr, cc) != (r, c):
                warehouse[rr][cc] = warehouse[rr - dr][cc - dc]
                rr -= dr
                cc -= dc
            r += dr
            c += dc

print("\n".join(["".join(row) for row in warehouse]))

total = 0
for i in range(R):
    for j in range(C):
        if warehouse[i][j] == box:
            total += 100 * i + j

print(total)
