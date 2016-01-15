import sys
from math import inf
from collections import defaultdict
from heapq import heappush, heappop

SQUARE_NUM = 100
DICE_RANGE = 6
INFINITY = inf

def getLeastMoves(ladders, snakes):
    G = drawGraph(ladders, snakes)
    # for k, v in G.items():
    #     print(str(k) + ":" + str(v))
    A = dijkstra(G, 1)
    return A[SQUARE_NUM]
    pass

def drawGraph(ladders, snakes):
    G = defaultdict(dict)
    # triggers contain ladder base and snake mouth,
    # which will trigger a move
    # ends contain ladder top and snake tail,
    # where a triggered move arrives
    # each ladder or snake is an edge of weight 1
    triggers = []
    ends = []
    for k, v in ladders.items():
        triggers.append(k)
        ends.append(v)
        G[k][v] = 0
    for k, v in snakes.items():
        triggers.append(k)
        ends.append(v)
        G[k] = {}
        G[k][v] = 0
    # draw graph
    src = 1
    dest = SQUARE_NUM
    # draw edges from src or to dest 
    for t in triggers:
        G[src][t] = getWeight(src, t, triggers)
    for e in ends:
        G[e][dest] = getWeight(e, dest, triggers)
    # draw edges from an end to a trigger, if the end is before the trigger
    for e in ends:
        for t in triggers:
            if e < t:
                G[e][t] = getWeight(e, t, triggers)
    print(G)
    return G
    pass

def getWeight(start, end, triggers):
    weight = 0
    triggerIn = []
    for t in triggers:
        if t > start and t < end:
            triggerIn.append(t)
    triggerIn.sort()
    current = start
    while current < end:
        for i in range(DICE_RANGE, -1, -1):
            if (current + i) not in triggerIn:
                break
        if i == 0:
            return INFINITY
        current += i
        weight += 1
    return weight
    pass

def dijkstra(graph, start):
    vertice = []
    for k, v in graph.items():
        if k not in vertice:
            vertice.append(k)
        for kk in graph[k].keys():
            if kk not in vertice:
                vertice.append(kk)
    # print(vertice)
    A = {}
    for v in vertice:
        A[v] = None
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))
    return A
    pass

def main():
    T = int(input().strip())
    for a0 in range(T):
        ladders = {}
        l = int(input().strip())
        for ll in range(l):
            temp = input().split()
            ladders[int(temp[0])] = int(temp[1])
        snakes = {}
        s = int(input().strip())
        for ss in range(s):
            temp = input().split()
            snakes[int(temp[0])] = int(temp[1])
        m = getLeastMoves(ladders, snakes)
        if m != INFINITY:
            print(m)
        else:
            print("-1")
        pass

if __name__ == "__main__":
    sys.exit(main())
