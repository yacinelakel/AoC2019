import math



def solve():
    f = open("input/day1.txt", "r")

    ans1 = 0
    ans2 = 0
    for l in f:
        x = int(l)
        ans1 += calc_fuel(x)
        ans2 += calc_fuel_fuel(x)

    f.close()

    print("Part 1: ", ans1)
    print("Part 2: ", ans2)


def calc_fuel(n):
    return math.floor(n / 3) - 2

def calc_fuel_fuel(n):
    f =  max(0, calc_fuel(n))
    total = f
    while f > 0:
        f = max(0, calc_fuel(f))
        total += f;
    return total

solve()