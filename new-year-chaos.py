import sys

def countChaos(diff, q):
    count = 0
    p = 0
    r = 0
    while p < len(diff):
        if diff[p] > 0:
            k = diff[p]
            r = p
            while k != 0:
                r += 1
                k += diff[r]
            count += countSwaps(q[p:r+1])
            p = r + 1
        else:
            p += 1
    return count
    pass

def countSwaps(q):
    count = 0
    for i in range(1, len(q)):
        key = q[i]
        j = i-1
        while j >= 0 and q[j] > key:
            q[j+1] = q[j] 
            j -= 1
            count += 1
        q[j+1] = key
    return count
    pass

def main():
    T = int(input().strip())
    for a0 in range(T):
        n = int(input().strip())
        q = [int(q_temp) for q_temp in input().strip().split(' ')]
        # your code goes here
        init = [i for i in range(1, n+1)]
        diff = [b - a for a,b in zip(init, q)]
        # print(diff)
        chaos = False
        for d in diff:
            if d > 2:
                chaos = True
                break
        if chaos:
            print("Too chaotic")
        else:
            print(countChaos(diff, q))
    pass

if __name__ == "__main__":
    sys.exit(main())