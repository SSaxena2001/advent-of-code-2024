from typing import List

res = 0


def valid(target: int, seq: List[int]) -> bool:
    if len(seq) == 1:
        return target == seq[0]
    if target % seq[-1] == 0 and valid(target // seq[-1], seq[:-1]):
        return True
    if target > seq[-1] and valid(target - seq[-1], seq[:-1]):
        return True
    str_t = str(target)
    str_l = str(seq[-1])
    # remove this check for part 1 answer
    if (
        len(str_t) > len(str_l)
        and str_t.endswith(str_l)
        and valid(int(str_t[: -len(str_l)]), seq[:-1])
    ):
        return True
    return False


for line in open(0):
    left, right = line.strip().split(": ")
    left = int(left)
    right = list(map(int, right.split()))

    if valid(left, right):
        res += left


print(res)
