m=[]
for i in range(256):
    l=list(map(int,input().split(" ")))
    m.append(l)
tla=[]
tra=[]
blc=[]
brc=[]
for i in range(256):
    for j in range(256):
        if m[i][j]==0:
            if len(tla)==0:
                tla.append(i)
                tla.append(j)
            else:
                tla[0]=min(i,tl[0])
                tla[1]=min(j,tl[1])
            if len(tra)==0:
                tra.append(i)
                tra.append(j)
            else:
                tra[0]=min(i,tra[0])
                tra[1]=max(j,tra[1])
            if len(blc)==0:
                blc.append(i)
                blc.append(j)
            else:
                blc[0]=max(i,blc[0])
                blc[1]=min(j,blc[1])
            if len(brc)==0:
                brc.append(i)
                brc.append(j)
            else:
                brc[0]=max(i,brc[0])
                brc[1]=max(j,brc[1])
print(tuple(tla),tuple(tra),tuple(blc),tuple(brc))
