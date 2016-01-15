import sys

def largestDecentNum(n):
	num = -1
	q, r = divmod(n, 3)
	if r == 1:
		if q >= 3:
			q -= 3
		else:
			return num
	elif r == 2:
		if q >= 1:
			q -= 1
		else:
			return num
	num = int('5'*q*3 + '3'*(n-q*3))
	return num
	pass

def main():
	t = int(input().strip())
	for a0 in range(t):
	    n = int(input().strip())
	    print(largestDecentNum(n))
	pass

if __name__ == "__main__":
	sys.exit(main())