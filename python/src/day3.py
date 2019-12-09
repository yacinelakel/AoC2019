import functools

def solve():
 f = open("inputs/day3.txt")
 lines = f.readlines()
 f.close()

 path_a = parse_line_to_points(lines[0])
 path_b = parse_line_to_points(lines[1])

 print('Part 1:', solve_part_one(path_a, path_b))
 print('Part 2:', solve_part_two(path_a, path_b))


def solve_part_one(path_a, path_b):
    intersections = []
    for i in range(0, len(path_b)-1):
        p2, p3 = (path_b[i], path_b[i+1])
        for j in range(0, len(path_a)-1):
            p0,p1 = (path_a[j], path_a[j+1])
            res = intersection(p0, p1, p2, p3)
            if res:
                intersections.append(res[1])
    distances = [abs(p[0]) + abs(p[1]) for p in intersections]
    return functools.reduce(lambda a,b : a if a != 0 and a < b else b, distances)

def solve_part_two(path_a, path_b):
    inter_a = steps_to_first_inter(path_a, path_b)
    inter_b = steps_to_first_inter(path_b, path_a)
    
    inter_sum = {}
    for key in inter_a:
        inter_sum[key] = inter_a[key] + inter_b[key]
    
    return min(inter_sum.items(), key=lambda x: x[1])[1]


def steps_to_first_inter(path_a, path_b):
    inter_dict = {}
    for i in range(0, len(path_a)-1):
        p0, p1 = (path_a[i], path_a[i+1])
        for j in range(0, len(path_b)-1):
            p2,p3 = (path_b[j], path_b[j+1])
            res = intersection(p0, p1, p2, p3)
            if res and res[1] != (0,0):
                path_a_s = path_a[0:i+1] + [res[1]]
                sum = 0
                for k in range(0, len(path_a_s)-1):
                    a,b = path_a_s[k], path_a_s[k+1]
                    sum += abs(b[0] - a[0]) + abs(b[1]-a[1])
                inter_dict[res[1]] = inter_dict.get(res[1], sum)
    return inter_dict                

def parse_line_to_points(line):
    path = line.split(',')
    pos = (0,0)
    points = [pos]
    for dir, *l  in path:
        cur_p = dir_to_point(pos, dir, int(''.join(l)))
        points.append(cur_p)
        pos = cur_p
    return points
    
def dir_to_point(pos, dir, dist):
    switcher = {
        'R': lambda p, d : (p[0] + d, p[1]), 
        'L': lambda p, d : (p[0] - d, p[1]),
        'U': lambda p, d : (p[0], p[1] + d),
        'D': lambda p, d : (p[0], p[1] -d)
    }
    return switcher.get(dir)(pos,dist)

def intersection(p0, p1, p2, p3):
    #https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
    s1 = (p1[0] - p0[0], p1[1]  - p0[1])
    s2 = (p3[0] - p2[0], p3[1]  - p2[1])
    
    d = (-s2[0] * s1[1] + s1[0] * s2[1]) 

    #Do not consider collinear or parallel lines
    if d == 0: return False
    
    s = (-s1[1] * (p0[0] - p2[0]) + s1[0] * (p0[1] - p2[1])) / d
    t = (s2[0] * (p0[1] - p2[1]) - s2[1] * (p0[0] - p2[0]))  / d

    if s >= 0 and s <= 1 and t >= 0 and t<= 1:
        return True, (int(p0[0] + (t * s1[0])), int(p0[1] + (t * s1[1])))
    
    return (False)


solve()
