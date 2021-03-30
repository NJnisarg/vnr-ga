import math
from geneticMetaheuristics import initialPopulation, crossover, mutate, populationSelection

def bestReconfig(SN, VN, GD, RD, N, Nmax, f):
    P = initialPopulation(GD, N)
    print("Initial Population", P)
    for i in range(0,Nmax):
        for j in range(0, N):
            for k in range(j+1, N):
                c = crossover(P[j],P[k])
                if c is not None:
                    P.append(c[0])
                    P.append(c[1])
        P = populationSelection(P, N, VN, GD, RD)
        if(i%f == 0):
            for j in range(0,N):
                P.append(mutate(P[j], RD))
            P = populationSelection(P, N, VN, GD, RD)
    return populationSelection(P, 1, VN, GD, RD)[0]

def migrate(SN, resources, VN, Sb):
    possible = False

    for i in range(0, len(Sb)):
        reqCpu = VN["nodeArr"][Sb[i]][0]
        reqMem = VN["nodeArr"][Sb[i]][1]
        reqCapacity = 0
        for j in range(0, len(VN["nodeArr"])):
            reqCapacity += VN["adjMat"][Sb[i]][j]
        
        residualResIdx = 0
        minRes = math.inf
        for j in range(0, len(resources)):
            if(resources[j][0] > reqCpu and resources[j][1] > reqMem and resources[j][2] > reqCapacity):
                possible = True
                residualRes = math.sqrt(((resources[j][0]-reqCpu)**2) + ((resources[j][1]-reqMem)**2) + ((resources[j][2]-reqCapacity)**2))
                if residualRes < minRes:
                    minRes = residualRes
                    residualResIdx = j
        
        if(not possible):
            return possible
        resources[residualResIdx][0] -= reqCpu
        resources[residualResIdx][1] -= reqMem
        resources[residualResIdx][2] -= reqCapacity
    
    return True

        