import sys

def main():
	T = int(input().strip())
	for a0 in range(0, T):
		n = int(input().strip())
		a = int(input().strip())
		b = int(input().strip())
		lastStone = []
		for i in range(0, n):
			stone = a*i + b*(n-1-i)
			if stone not in lastStone:
				lastStone.append(stone)
		res = " ".join(str(s) for s in sorted(lastStone))
		print(res)
	pass

if __name__ == "__main__":
	sys.exit(main())