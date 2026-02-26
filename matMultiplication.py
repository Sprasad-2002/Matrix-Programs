m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[1,4,4],[1,2,1],[1,0,0]]
res=[]
if len(m1)==0 and len(m2)==0:
    print(m1)
elif (len(m1)>0 and len(m2)>0 ) and len(m1[0])==len(m2):
    for ind1 in range(len(m1)):
        line=[]
        for ind2 in range(len(m1[0])):
            value=0
            for ind3 in range (len(m2)):
                value+=m1[ind1][ind3]*m2[ind3][ind2]
            line.append(value)
        res.append(line)
    print(res)
else:
    print('Not Possible')