import sys

SQUARE_NUM = 100
DICE_RANGE = 6

def getLeastMoves(ladders, snakes):
	G = drawGraph(ladders, snakes)
	p, v = dijkstra(G, 1, 100)
	return v
	pass

def drawGraph(ladders, snakes):
	G = {}
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
		G[k][v] = 1
	for k, v in snakes.items():
		triggers.append(k)
		ends.append(v)
		G[k][v] = 1
	# draw graph
	src = 1
	dest = SQUARE_NUM
	# draw edges from src or to dest 
	for t in triggers:
		G[src][t] = getWeight(src, t)
	for e in ends:
		G[e][dest] = getWeight(e, dest)
	# draw edges from an end to a trigger, if the end is before the trigger
	for e in ends:
		for t in triggers:
			if e < t:
				G[e][t] = getWeight(e, t)
	return G
	pass

def getWeight():
	pass

def dijkstra(aGraph, start, end):

	pass

def main():
	T = int(input().strip())
	for a0 in range(T):
		ladders = {}
		l = int(input().strip())
		for ll in range(l):
			temp = input().split()
			ladders[temp[0]] = temp[1]
		snakes = {}
		s = int(input().strip())
		for ss in range(s):
			temp = input().split()
			snakes[temp[0]] = temp[1]
		getLeastMoves(ladders, snakes)
		# print(moves)
		pass

if __name__ == "__main__":
	sys.exit(main())