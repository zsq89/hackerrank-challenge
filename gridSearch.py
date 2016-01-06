'''
The grid search:
search a block pattern in a matrix of digits
return YES if the pattern is found, NO otherwise
'''

import sys

def isInGrid(G, P):
    gr = len(G)
    gc = len(G[0])
    pr = len(P)
    pc = len(P[0])
    for i in range(0, gr-pr+1):
        for j in range(0, gc-pc+1):
            subG = getSubGrid(G, i, j, pr, pc)
            if compareBlock(P, subG):
                return True
    return False
    pass  

def compareBlock(G1, G2):
    for r1, r2 in zip(G1, G2):
        if r1 != r2:
            return False
    return True
    pass

def getSubGrid(G, i, j, r, c):
    subG = []
    for k in range(r):
        subG.append(G[i+k][j:j+c])
    return subG
    pass

def main():
    t = int(input().strip())
    for a0 in range(t):
        R,C = input().strip().split(' ')
        R,C = [int(R),int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
            G_t = str(input().strip())
            G.append(G_t)
        r,c = input().strip().split(' ')
        r,c = [int(r),int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
            P_t = str(input().strip())
            P.append(P_t)
    # G = ["123","245","597"]
    # P = ["24","59"]
    if isInGrid(G, P):
        print("YES")
    else:
        print("NO")
    pass

if __name__ == "__main__":
    sys.exit(main())


