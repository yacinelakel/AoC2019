def get_orbit_map():
    orbit_map = {}
    with open("inputs/day6.txt", "r") as file:
        for line in file:
           l = line.rstrip('\n').split(")")
           orbit_map[l[0]] = orbit_map.get(l[0], []) + [l[1]]
           orbit_map[l[1]] = orbit_map.get(l[1], []) + [l[0]]
    return orbit_map

def bfs(orbit_map, start="COM", stop=None):
    visited = {start: 1}
    queue = [(start,0)]
    orbits = 0
    while len(queue) != 0:
        node, depth = queue.pop()
        orbits += depth
        adj = orbit_map.get(node, [])
        for n in adj:
            if stop != None and n == stop:
                return depth - 1
            if not visited.get(n, 0):
                queue.append((n, depth+1))
                visited[n] = 1
    return orbits

def solve():
    orbit_map = get_orbit_map()

    print('Part 1: ', bfs(orbit_map))
    print('Part 2: ', bfs(orbit_map,"YOU", "SAN"))

solve()