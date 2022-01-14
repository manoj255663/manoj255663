l1=[1,2,3,4]
l2=[1,2,5,4]
j=0
for i in range(len(l1)):
    if(l1[i]==l2[i]):
        j=j+1
if(j==len(l1)):
    print("1")
else:
    print("-1");
