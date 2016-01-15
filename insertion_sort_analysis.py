import sys

def countMoves(arr, n):
	moves = 0

	pass


def main():
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		arr = [int(num) for num in input().split()]
		moves = countMoves(arr, n)
		print(moves)
	pass

if __name__ == "__main__":
	sys.exit(main())