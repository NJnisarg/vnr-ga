import random
import heapq

def perm_generator(seq):
    seen = set()
    length = len(seq)
    while True:
        perm = tuple(random.sample(seq, length))
        if perm not in seen:
            seen.add(perm)
            yield perm

def initialPopulation(GD, N):
    rand_perms = perm_generator(list(GD))
    P0 = [next(rand_perms) for _ in range(N)]
    return P0

def sim(s1,s2):
    n = len(s1)
    s = [0 for i in range(n)]
    for i in range(0,n):
        if(s1[i] == s2[i]):
            s[i] = 1
    return s

def hamming(sim):
    h = 0
    for i in range(0, len(sim)):
        if(sim[i] == 1):
            h+=1
    
    return h

def crossover(s1,s2):
    n = len(s1)
    s = sim(s1,s2)
    h = hamming(s)
    if(h >= 2):
        firstOne = -1
        secondOne = -1
        for i in range(0, len(s)):
            if(s[i] == 1):
                if(firstOne == -1):
                    firstOne = i
                secondOne = i            
        alpha = secondOne - firstOne

        c1 = [0 for i in range(n)]
        c2 = [0 for i in range(n)]
        for i in range(n):
            if(i < alpha):
                c1[i] = s1[i]
                c2[i] = s2[i]
            else:
                c1[i] = s2[i]
                c2[i] = s1[i]
        
        return (c1, c2)
    return None

def mutate(S, RD):
    nodeToRem = set()
    nodeToKeep = set()
    for i in range(0, len(RD)):
        if(RD[i][0] not in nodeToKeep):
            nodeToRem.add(RD[i][0])
        nodeToKeep.add(RD[i][1])
    
    newS = [S[i] for i in range(0, len(S))]
    for i in range(0, len(S)):
        if(S[i] in nodeToRem):
            newS[i] = 0
    
    return tuple(newS)

def fScore(S, VN, GD, RD):
    a=0.5
    b=0.5
    alph=0.5
    beta=0.5

    phiN = 0
    phiE = 0
    
    for i in range(0, len(S)):
        if(S[i] > 0):
            phiN+=1
    for i in range(0, len(RD)):
        phiE += (RD[i][2] + random.randint(1,5))
    
    phiD = a*phiN + b*phiE

    psiD = 0
    for i in range(0, len(VN["nodeArr"])):
        for j in range(0,random.randint(1,5)):
            psiD += VN["nodeArr"][i][0]
    
    return 1/(alph*phiD + beta*psiD + random.uniform(0,1)); 

def populationSelection(P, N, VN, GD, RD):
    potentialP = [[P[i], 0] for i in range(0, len(P))]
    for i in range(0, len(P)):
        if P[i] is None:
            continue
        potentialP[i][1] = fScore(P[i], VN, GD, RD)
    potentialP = sorted(potentialP,key=lambda x: x[1], reverse=True)
    ans = []
    for i in range(0,N):
        ans.append(potentialP[i][0])
    
    return ans
