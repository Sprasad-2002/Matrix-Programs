m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,4,4],[1,2,1],[1,0,0]]
res=[]
if len(m1)==0 and len(m2)==0:
    print(m1)
elif (len(m1)==len(m2)) and (len(m1[0])==len(m2[0])):
    for ind1 in range(len(m1)):
        for ind2 in range(len(m1[0])):
            m1[ind1][ind2]=m1[ind1][ind2]+m2[ind1][ind2]
    print(m1)
else:
    print('not possible')