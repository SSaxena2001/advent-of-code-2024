import re


def part1(input: str):
    pattern = r"mul\(\d+,\d+\)"

    matches = re.findall(pattern, input)

    pairs = [tuple(map(int, match[4:-1].split(","))) for match in matches]

    return sum([a * b for a, b in pairs])


def part2(input: str) -> int:
    pattern = r"(mul\(-?\d+\.?\d*,-?\d+\.?\d*\)|do\(\)|don\'t\(\))"

    matches = re.findall(pattern, input)

    filtered_lst = []
    do_found = True
    for item in matches:
        if item == "do()":
            do_found = True
            continue
        elif item == "don't()":
            do_found = False
            continue

        if do_found:
            filtered_lst.append(item)

    pairs = [tuple(map(int, match[4:-1].split(","))) for match in filtered_lst]

    return sum([a * b for a, b in pairs])


if __name__ == "__main__":
    input = open(0).read().strip()

    print(part1(input))
    print(part2(input))
