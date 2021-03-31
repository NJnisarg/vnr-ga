import random
import matplotlib
import matplotlib.pyplot as plt
from graphBuild import buildNetwork, generateSolutionComponents, computeResource, plotMetrics
from vnrFramework import bestReconfig, migrate, unallocate

def simulate():
    metrics = {
        "Qu": [0],
        "Qv": [0],
        "Ctot": [0]
    }
    SN = buildNetwork(100, 50, 100, 50, 100)
    resources = computeResource(SN)
    diffQueue = []
    doAdd = False
    T = 0
    while(T<5000):
        if(T%25==0): # 4 requests every 100 sec
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
            print("Time",T)
            GD = generateSolutionComponents(SN, VN, RD)
            print("n,GD", n, GD)
            Sb = bestReconfig(SN, VN, GD, RD, 20, 20, 5, metrics)
            print("SB", Sb)
            didMigrate = migrate(SN, resources, VN, Sb, diffQueue, metrics)
            print("DidMigrate", didMigrate)
            if(not didMigrate):
                doAdd = True
            else:
                doAdd = False
            print("====================================")
        T+=1

    plotMetrics(metrics)


simulate()