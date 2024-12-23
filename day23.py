from collections import defaultdict

edges = [line.strip().split("-") for line in open(0)]

network = defaultdict(set)

for x, y in edges:
    network[x].add(y)
    network[y].add(x)

seen = set()


def part2():
    def search(node, req):
        key = tuple(sorted(req))
        if key in seen:
            return
        seen.add(key)
        for neighbor in network[node]:
            if neighbor in req:
                continue
            if not all(neighbor in network[query] for query in req):
                continue
            search(neighbor, {*req, neighbor})

    for x in network:
        search(x, {x})

    print(",".join(sorted(max(seen, key=len))))
    exit(0)


part2()


# Part 1 code
for x in network:
    for y in network[x]:
        for z in network[y]:
            if (
                x != z
                and x in network[z]
                and any(cn.startswith("t") for cn in [x, y, z])
            ):
                seen.add(tuple(sorted([x, y, z])))

print(len([s for s in seen if any(cn.startswith("t") for cn in s)]))
