import sys
from math import pow

def main():
	T = int(input().strip())
	for a0 in range(0, T):
		n = int(input().strip())
		w = []
		while n > 0:
			[a,b] = divmod(n, 3)
			if b == 0:
				w.append(0)
				n = a
			elif b == 1:
				w.append(1)
				n = a
			else:
				w.append(-1)
				n = a + 1
		left = 'left pan:'
		right = 'right pan:'
		for i in range(len(w)-1, -1, -1):
			if w[i] < 0:
				left += ' ' + str(int(pow(3, i)))
			elif w[i] > 0:
				right += ' ' + str(int(pow(3, i)))
		print(left)
		print(right)
		if a0 < T-1:
			print('')
	pass

if __name__ == "__main__":
	sys.exit(main())