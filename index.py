import random
from graphBuild import buildNetwork, generateSolutionComponents, computeResource
from vnrFramework import bestReconfig, migrate

def simulate():
    SN = buildNetwork(100, 50, 100, 50, 100)
    resources = computeResource(SN)
    T = 0
    while(True):

        T+=1
    n = random.randint(4,10) # number of virtual nodes
    VN = buildNetwork(n, 10, 20, 10, 20)

    RD = []
    numLinks = 0
    for i in range(0, n):
        for j in range(0,n):
            if(VN["adjMat"][i][j] > 0):
                numLinks+=1
    numUpgradedLinks = random.randint(1,numLinks)
    ratio = numUpgradedLinks/numLinks
    for i in range(0, n):
        for j in range(i, n):
            if (random.uniform(0,1) < ratio):
                RD.append((i,j, random.uniform(1.1,2)*VN["adjMat"][i][j]))
    
    GD = generateSolutionComponents(SN, VN, RD)
    print("GD", GD)
    Sb = bestReconfig(SN, VN, GD, RD, 20, 20, 5)
    print("SB", Sb)
    migrate(SN, resources, VN, Sb)


simulate()