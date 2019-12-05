import functools
import itertools

def validate(password):
    d = {}
    adjFound = False
    for i in range(0, len(password)-1):
        if password[i] == password[i+1]:
            d[password[i]] = d.get(password[i], 1) + 1
            adjFound = True
        if int(password[i]) > int(password[i+1]):
            return (False, False)

    return (adjFound, 2 in d.values())

def solve(r1, r2):
    res = functools.reduce(lambda acc, cur: (lambda a, v: (a[0]+1 if v[0] else a[0], a[1]+1 if v[1] else a[1]))(acc,validate(str(cur))), range(r1,r2), (0,0))

    print('Part 1:', res[0])
    print('Part 2:', res[1])


solve(359282, 820401)


