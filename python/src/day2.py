def solve():
    f = open("input/day2.txt");
    program = [int(i) for i in f.readline().split(",")]
    f.close()
    print("Part 1: ", solve_part_one(program))
    print("Part 2: ", solve_part_two(program))
                
def solve_part_two(program):
    for noun in range(100):
        for verb in range(100):
            cur_program = program[:]
            cur_program[1] = noun
            cur_program[2] = verb
            if run_program(cur_program)[0] == 19690720:
                return 100 * noun + verb

def solve_part_one(program):
    fixed_program = program[:]
    fixed_program[1] = 12
    fixed_program[2] = 2
    return run_program(fixed_program)[0]

def run_program(program, input):
    result = program[:]
    pos = 0;
    opcode = result[pos];
    while opcode != 99:
        if opcode == 1:
            result[result[pos+3]] = result[result[pos+1]] + result[result[pos+2]]
        elif opcode == 2:
            result[result[pos+3]] = result[result[pos+1]] * result[result[pos+2]]
        pos = pos + 4;
        opcode = result[pos];
    return result;

solve()
         