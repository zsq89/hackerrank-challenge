import sys

def getMinUnfairness(candy, n, k):
	quickSort(candy, 0, n-1)
	print(candy)
	m = minUnfair(candy[0:k])
	for i in range(1, n-k+1):
		temp = minUnfair(candy[i:i+k])
		if temp < m:
			m = temp
	return m
	pass

def minUnfair(c):
	m = 0
	l =len(c)
	p = int(l / 2)
	for i in range(p):
		m += (c[l-1-i] - c[i]) * (l - 1 - i * 2)
	return m

def quickSort(aList, p, r):
	if p >=r:
		return
	else:
		q = partitionList(aList, p, r)
		quickSort(aList, p, q-1)
		quickSort(aList, q+1, r)

def partitionList(aList, p, r):
	# Choose aList[r] as the pivot
	# k is used to trace the leftmost index of right partition
	k = p
	for i in range(p, r):
		if aList[i] < aList[r]:
			# if aList[i] comes before the pivot,
			# swap it with the leftmost of right partition, i.e. aList[k]
			# since left partition increases by 1, shift k to the right by 1
			temp = aList[k]
			aList[k] = aList[i]
			aList[i] = temp
			k += 1
	# after partition, swap the pivot with the element at k
	# return the index of pivot
	temp = aList[k]
	aList[k] = aList[r]
	aList[r] = temp
	return k

def main():
	n = int(input().strip())
	k = int(input().strip())
	candy = []
	for i in range(n):
		candy.append(int(input().strip()))
	unfairMin = getMinUnfairness(candy, n, k)
	print(unfairMin)
	pass

if __name__ == "__main__":
	sys.exit(main())