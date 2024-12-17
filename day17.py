import re


def combo_operand_val(operand, regVals) -> int:
    return [0, 1, 2, 3, regVals[0], regVals[1], regVals[2], -1][operand]


def process_instruction(idx, instructions, regVals):
    if idx >= len(instructions):
        return None

    op_code = instructions[idx]
    operand = instructions[idx + 1]

    match op_code:
        case 0:
            val = combo_operand_val(operand, regVals)
            regVals[0] = regVals[0] >> val
        case 1:
            regVals[1] ^= operand
        case 2:
            regVals[1] = combo_operand_val(operand, regVals) % 8
        case 3:
            if regVals[0] == 0:
                return None
            else:
                return -1
        case 4:
            regVals[1] ^= regVals[2]
        case 5:
            return combo_operand_val(operand, regVals) % 8
        case 6:
            val = combo_operand_val(operand, regVals)
            regVals[1] = regVals[0] >> val
        case 7:
            val = combo_operand_val(operand, regVals)
            regVals[2] = regVals[0] >> val
        case _:
            raise ValueError("Invalid op_code")

    return None


def part1():
    regVals, instructions = open(0).read().split("\n\n")

    regVals = list(map(int, re.findall(r"\d+", regVals)))
    instructions = list(map(int, instructions[8:].split(",")))
    idx = 0
    outputs = []
    while idx != len(instructions):
        res = process_instruction(idx, instructions, regVals)
        if res is not None and res != -1:
            outputs.append(res)
        if res == -1:
            idx = instructions[idx + 1]
        else:
            idx += 2

    print(outputs)
    print(*outputs, sep=",")


part1()


"""

b = a % 8
b = b ^ 3
c = a >> b
a = a >> 3
b = b ^ a
b = b ^ c
out(b % 8)
a != 0 jump 0


"""
