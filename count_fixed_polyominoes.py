from math import sqrt
import pprint
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)
parser.add_argument('-p', action='store_true')
args = parser.parse_args()
p = args.p
n = args.n
n = int(n)
V = (n * (n - 1)) + 1
nodes = []
graph = {}
for i in range(-n, n):
    for j in range(-1, n):
        if((j > 0) or (j == 0) and i >= 0):
            if abs(i) + abs(j) < n:
                nodes.append((i,j))
for a in range(V):
    adjlist = []
    for b in range(V):
        if (b > a + n or len(adjlist) == 4):
            break
        else:
            distance = sqrt((nodes[b][0] - nodes[a][0]) ** 2 + (nodes[b][1] - nodes[a][1]) ** 2)
            if (distance == 1):
                adjlist.append(nodes[b])
    graph[nodes[a]] = adjlist
if p:
    pprint.pprint(graph)
def NeighborVInP(graph, p, u, posv):
    sen = False
    counter = 0
    for f in p:
        posp = p.index(f)
        dist = sqrt((graph[u][posv][0] - p[posp][0]) ** 2 + (graph[u][posv][1] - p[posp][1]) ** 2)
        if dist == 1:
            counter = counter + 1
    if counter == 1:
        sen = True
    return sen
untried = [(0,0)]
p = []
c = 0
def add():
    global c
    c += 1
def CountFixedPolyominoes(graph, untried, n, p, c):
    while len(untried) != 0:
        u = untried.pop()
        p.append(u)
        if len(p) == n:
            add()
        else:
            new_neighbors = []
            for v in graph[u]:
                 posv = graph[u].index(v)
                 if (v not in untried) and (v not in p) and NeighborVInP(graph, p, u, posv):
                     new_neighbors.append(v)
            new_untried = untried + new_neighbors
            CountFixedPolyominoes(graph, new_untried, n, p, c)
        p.remove(u)    
    return c
CountFixedPolyominoes(graph, untried, n, p, c)
print(c)