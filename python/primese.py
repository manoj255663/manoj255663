"""def primeseries():
    i=0
    while i<100:
        j=2
        flag=0
        while j<i:
            if(i%j==0):
                flag=1
            j=j+1
        if(flag==0):
            print(i)
        i=i+1
primeseries()
"""
"""
n=int(input("enter a number: "))
str1=str(n)
str2=str1[::-1]
print(str2)
if str1==str2:
    print("palindrome")
else:
    print("not palindrome")
"""
num=int(input("enter a number: "))
bools=True
for i in range(2,num):
    if num%i==0:
        bools=False
        break
    else:
        bools=True
if bools==True:
    print("is prime")
else:
    print("not prime")
