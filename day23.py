from collections import defaultdict

edges = [line.strip().split("-") for line in open(0)]

network = defaultdict(set)

for x, y in edges:
    network[x].add(y)
    network[y].add(x)

seen = set()

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
