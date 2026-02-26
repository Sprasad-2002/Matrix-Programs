m1=[[1,2,3],[4,5,6],[7,8,9]]
ans=[]
for ind1 in range(len(m1)):
    ele=[]
    for ind2 in range(len(m1[0])-1,-1,-1):
        ele.append(m1[ind2][ind1])
        
    ans.append(ele)
print(ans)