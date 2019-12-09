from aocd.models import Puzzle
from collections import defaultdict

orbitalMap = defaultdict(list)


def buildMap(orbits):
    systemMap = defaultdict(list)
    for orbit in orbits:
        mass, sat = orbit.split(')')
        systemMap[mass].append(sat)

    return systemMap


def sumOrbits(systemMap, mass, d=0):
    # print(f"{mass} has {d} orbits")
    totalorbits = d
    toVisit = [(sat, d+1) for sat in systemMap[mass]]

    while toVisit:
        visiting, toVisit = toVisit[0], toVisit[1:]
        mass, d = visiting
        toVisit += [(sat, d+1) for sat in systemMap[mass]]
        totalorbits += d

    return totalorbits


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


if __name__ == "__main__":
    # Get Puzzle data
    p = Puzzle(year=2019, day=6)
    input_data = p.input_data.splitlines()

    systemMap = buildMap(input_data)

    print(sumOrbits(systemMap, 'COM'))

    p2you = find_path(systemMap, 'COM', 'YOU')
    p2san = find_path(systemMap, 'COM', 'SAN')

    print(len(set(p2you) ^ set(p2san)) - 2)
