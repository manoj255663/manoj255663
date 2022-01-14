n="13578"
a=[]
d=[]
for i in range(0,5):
    c=int(n[i])
    a.append(c)

for j in range(0,4):
    if (a[j]<int(a[j+1])):
        d.append(a[j])
        x=true
    else:
        print("not in increasing order")
print(d)

