import random

def buildNetwork(N, linkCapacityR1, linkCapacityR2, resCapacityR1, resCapacityR2):
    adjMat = [[0 for x in range(N)] for y in range(N)]
    nodeArr = [(0,0) for x in range(N)] # (cpu, mem) 
    for i in range(0,N):
        for j in range(i,N):
            val = random.uniform(0,1)
            if(val > 0.5):
                linkCapacity = random.randint(linkCapacityR1, linkCapacityR2)
                adjMat[i][j] = linkCapacity
                adjMat[j][i] = linkCapacity
        cpu = random.randint(resCapacityR1, resCapacityR2)
        mem = random.randint(resCapacityR1, resCapacityR2)
        nodeArr[i] = (cpu, mem)
    return {"nodeArr": nodeArr, "adjMat":adjMat}

def computeResource(SN):
    resources = [] # (cpu, mem, capacity)
    for i in range(0, len(SN["nodeArr"])):
        cpu = SN["nodeArr"][i][0]
        mem = SN["nodeArr"][i][0]
        capacity = 0
        for j in range(0, len(SN["nodeArr"])):
            capacity += SN["adjMat"][i][j]
        resources.append([cpu,mem,capacity])
    return resources

def generateSolutionComponents(SN, VN, RD):
    n = len(VN["nodeArr"])
    numUpdates = len(RD) # An arr of the form (i,j, newCapacity)
    setOfCenters = set()
    GD = set()
    for i in range(0,numUpdates):
        setOfCenters.add(RD[i][0])
        setOfCenters.add(RD[i][1])
    for i in range(0,n):
        if(i in setOfCenters):
            GD.add(i) # Adding the node in the set GD
    
    return GD





