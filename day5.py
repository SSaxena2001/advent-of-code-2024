from typing import Dict, List, Tuple
from functools import cmp_to_key


def part1(sequences: List[List[int]], order_pairs: List[Tuple[int, ...]]):
    rules = get_orders_map(order_pairs)
    total = 0
    for seq in sequences:
        if is_safe(seq, rules):
            total += seq[len(seq) // 2]

    return total


def part2(sequences: List[List[int]], order_pairs: List[Tuple[int, ...]]):
    rules = get_orders_map(order_pairs)
    cmp_rules = get_orders_map2(order_pairs)

    def comparator(a: int, b: int):
        return cmp_rules.get((a, b), 0)

    total = 0
    for seq in sequences:
        if is_safe(seq, rules):
            continue
        seq.sort(key=cmp_to_key(comparator))
        total += seq[len(seq) // 2]

    return total


def is_safe(seq: List[int], orders_map: Dict[Tuple[int, int], bool]):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            key = (seq[i], seq[j])
            if key in orders_map and not orders_map[key]:
                return False
    return True


def get_orders_map(order_pairs: List[Tuple[int, ...]]):
    orders_map = {}
    for a, b in order_pairs:
        orders_map[(a, b)] = True
        orders_map[(b, a)] = False
    return orders_map


def get_orders_map2(order_pairs: List[Tuple[int, ...]]):
    orders_map = {}
    for a, b in order_pairs:
        orders_map[(a, b)] = -1
        orders_map[(b, a)] = 1
    return orders_map


if __name__ == "__main__":
    input = open(0).read().strip()

    order, sample = input.split("\n\n")

    order_pairs = [tuple(map(int, x.split("|"))) for x in order.splitlines()]
    sequences = [list(map(int, x.split(","))) for x in sample.splitlines()]

    # print(part1(sequences, order_pairs))
    print(part2(sequences, order_pairs))

    pass
