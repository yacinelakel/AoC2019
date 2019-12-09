from timeit import default_timer as timer


def get_program():
    f = open("inputs/day7.txt")
    program = [int(i) for i in f.readline().split(",")]
    f.close()
    return program

def run_amplifiers(program):
    max_thrust = 0
    for (A,B,C,D,E) in itertools.permutations(range(5)):
        out = run_amplifier_setting(A, B, C, D, E, program)
        max_thrust = max(max_thrust, out)
    return max_thrust

def run_amplifier_setting(phase_A, phase_B, phase_C, phase_D, phase_E, program):
    #todo
    return 0

def run_program(program, inp):
    pos, out = 0, []
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

import itertools 



