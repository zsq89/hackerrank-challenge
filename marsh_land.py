import sys

def maxPerimeter(land):
	
	return perim
	pass

def main():
	T = int(input().strip())
	for a0 in range(T):
		m, n = [int(temp) for temp in input().split()]
		land = []
		for i in range(m):
			row = [1 if temp == '.' else 0 for temp in input().split()]
			land.append(row)
		print(land)
	pass

if __name__ == "__main__":
	sys.exit(main())