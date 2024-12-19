towels, designs = open(0).read().split("\n\n")

towels = towels.split(", ")
designs = designs.splitlines()


def check_design(design, patterns, dp={}):
    if not design:
        return True

    if design in dp:
        return dp[design]

    for d in patterns:
        if design.startswith(d):
            rem = design[len(d) :]
            if check_design(rem, patterns, dp):
                dp[design] = True
                return True

    dp[design] = False
    return False


def count_ways(design, patterns, dp={}):
    if not design:
        return 1

    if design in dp:
        return dp[design]

    ways = 0
    for d in patterns:
        if design.startswith(d):
            rem = design[len(d) :]
            ways += count_ways(rem, patterns, dp)

    dp[design] = ways
    return ways


def part1(towels, designs):
    ans = sum(1 for design in designs if check_design(design, towels))
    print(ans)


def part2(towels, designs):
    ans = []
    for design in designs:
        ans.append(count_ways(design, towels))
    print(sum(ans))


part2(towels, designs)
