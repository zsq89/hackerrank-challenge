import sys

def getLeastMoves(squareNum, ladder, snake):
	pass

def main():
	SQUARE_NUM = 100
	T = int(input().strip())
	for a0 in range(0, T):
		ladder = []
		l = int(input().strip())
		for ll in range(0, l):
			ladder.append([int(e) for e in input.split()])
		snake = []
		s = int(input().strip())
		for ll in range(0, s):
			snake.append([int(e) for s=e in input.split()])
		moves = getLeastMoves(SQUARE_NUM, ladder, snake)
		print(moves)
	pass

if __name__ == "__main__":
	sys.exit(main())