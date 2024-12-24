file = open(0)

vals = {}
for line in file:
    if line.isspace():
        break
    x, y = line.split(": ")
    vals[x] = int(y)

eqs = {}

for line in file:
    x, op, y, z = line.replace(" -> ", " ").split()
    eqs[z] = (op, x, y)


operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
}


def calc(wire):
    if wire in vals:
        return vals[wire]
    op, x, y = eqs[wire]
    vals[wire] = operators[op](calc(x), calc(y))
    return vals[wire]


zs = []
i = 0

while True:
    key = "z" + str(i).rjust(2, "0")
    if key not in eqs:
        break

    zs.append(calc(key))
    i += 1

print(int("".join(map(str, zs[::-1])), 2))
