from timeit import default_timer as timer

def solve():
    program = get_program()
    print('Part 1: ', solve_part_one(program[:]))
    print('Part 2: ', solve_part_two(program[:]))

def get_program():
    f = open("input/day5.txt")
    program = [int(i) for i in f.readline().split(",")]
    f.close()
    return program

def solve_part_two(program):
    pos, inp, out = 0, 5, []
    while(program[pos] != 99):
        instruction = str(program[pos]).zfill(4)
        opcode, mode1, mode2 = instruction[2:], int(instruction[1]), int(instruction[0])
        if opcode == "01":
            res = opcode_1(program, pos, inp, out, mode1, mode2)
        elif opcode == "02":
            res = opcode_2(program, pos, inp, out, mode1, mode2)
        elif opcode == "03":
            res = opcode_3(program, pos, inp, out)
        elif opcode == "04":
            res = opcode_4(program, pos, inp, out, mode1)
        elif opcode == "05":
            res = opcode_5(program, pos, inp, out, mode1, mode2)
        elif opcode == "06":
            res = opcode_6(program, pos, inp, out, mode1, mode2)
        elif opcode == "07":
            res = opcode_7(program, pos, inp, out, mode1, mode2)
        elif opcode == "08":
            res = opcode_8(program, pos, inp, out, mode1, mode2)
        else:
            raise Exception("Invalid instruction " + instruction)
        program, pos, inp, out = res
    return out[-1]

def solve_part_one(program):
    pos, inp, out = 0, 1, []
    while(program[pos] != 99):
        instruction = str(program[pos]).zfill(4)
        opcode, mode1, mode2 = instruction[2:] ,int(instruction[1]), int(instruction[0])
        if opcode == "01":
            res = opcode_1(program, pos, inp, out, mode1, mode2)
        elif opcode == "02":
            res = opcode_2(program, pos, inp, out, mode1, mode2)
        elif opcode == "03":
            res = opcode_3(program, pos, inp, out)
        elif opcode == "04":
            res = opcode_4(program, pos, inp, out, mode1)
        else:
            raise Exception("Invalid instruction " + instruction)
        program, pos, inp, out = res
    return out[-1]

def opcode_1(program, pos, inp, out, m1, m2):
    arg1 = program[program[pos+1]] if m1 == 0 else program[pos+1]
    arg2 = program[program[pos+2]] if m2 == 0 else program[pos+2]
    program[program[pos+3]] = arg1 + arg2
    return (program, pos+4, inp, out)

def opcode_2(program, pos, inp, out, m1, m2):
    arg1 = program[program[pos+1]] if m1 == 0 else program[pos+1]
    arg2 = program[program[pos+2]] if m2 == 0 else program[pos+2]
    program[program[pos+3]] = arg1 * arg2
    return (program, pos+4, inp, out)

def opcode_3(program, pos, inp, out):
    program[program[pos+1]] = inp
    return (program, pos+2, inp, out)

def opcode_4(program, pos, inp, out, m1):
    out += [program[program[pos+1]]] if m1 == 0 else [program[pos+1]]
    return (program, pos+2, inp, out)
    
def opcode_5(program, pos, inp, out, m1, m2):
    arg1 = program[program[pos+1]] if m1 == 0 else program[pos+1]
    arg2 = program[program[pos+2]] if m2 == 0 else program[pos+2]
    return (program, arg2 if arg1 != 0 else pos+3, inp, out)

def opcode_6(program, pos, inp, out, m1, m2):
    arg1 = program[program[pos+1]] if m1 == 0 else program[pos+1]
    arg2 = program[program[pos+2]] if m2 == 0 else program[pos+2]
    return (program, arg2 if arg1 == 0 else pos+3, inp, out)

def opcode_7(program, pos, inp, out, m1, m2):
    arg1 = program[program[pos+1]] if m1 == 0 else program[pos+1]
    arg2 = program[program[pos+2]] if m2 == 0 else program[pos+2]
    program[program[pos+3]] = 1 if arg1 < arg2 else 0
    return (program, pos+4, inp, out)

def opcode_8(program, pos, inp, out, m1, m2):
    arg1 = program[program[pos+1]] if m1 == 0 else program[pos+1]
    arg2 = program[program[pos+2]] if m2 == 0 else program[pos+2]
    program[program[pos+3]] = 1 if arg1 == arg2 else 0
    return (program, pos+4, inp, out)

start = timer()
solve()
end = timer()
print(end - start)