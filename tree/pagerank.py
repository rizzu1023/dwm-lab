import numpy as np
N=int(input("\nhow many no pages:"))
print("\please enter the adjacency matrix for the network")
links = []
for i in range(0,N):
    L=[]
    for j in range(0,N):
        L.append(int(input()))
    links.append(L)  
outboundL=np.zeros(N,),dtype=int)
for i in range(0,N):
    for j in range(0,N):
        if(links[i][j]==1):
         outboundL[i]+=1