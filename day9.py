"""

Day 9

12345
0..111....22222
even id => file
odd => disk space

let's represent the file with it's val and disk space as -1
then we can move the data from right to left in our disk

022111222 -> we need to generate this string from 12345
for second part

we now need to consider the whole file as one,
we can't move it to the right as the file can break into pieces which are set in different disk spaces

so let's keep track of the file and size for it


"""


def part1():
    disk = []
    curr_id = 0

    for i, val in enumerate(input()):
        val = int(val)
        if i % 2 == 0:
            disk += [curr_id] * val
            curr_id += 1
        else:
            disk += [-1] * val

    spaces = [i for i, el in enumerate(disk) if el == -1]

    for space in spaces:
        while disk[-1] == -1:
            disk.pop()
        if len(disk) <= space:
            break
        disk[space] = disk.pop()

    print(sum(i * x for i, x in enumerate(disk)))


def part2():
    file_map = {}
    spaces = []
    curr_id = 0
    pos = 0

    for i, val in enumerate(input()):
        val = int(val)
        if i % 2 == 0:
            if val == 0:
                raise ValueError("File size can't be 0")
            file_map[curr_id] = (pos, val)
            curr_id += 1
        else:
            if val != 0:
                spaces.append((pos, val))
        pos += val

    while curr_id > 0:
        curr_id -= 1
        pos, size = file_map[curr_id]

        for i, (s, ll) in enumerate(spaces):
            if s >= pos:
                spaces = spaces[:i]
                break
            if size <= ll:
                file_map[curr_id] = (s, size)
                if size == ll:
                    spaces.pop(i)
                else:
                    spaces[i] = (s + size, ll - size)
                break

    res = 0
    for id, (pos, size) in file_map.items():
        for val in range(pos, pos + size):
            res += val * id

    print(res)


part2()
