def reverse():
    i=int(input("Enter Number ="))
    sum=0
    c=0
    while i>0:
        c=i%10
        sum=sum*10+c
        i=i//10
    print("rev number =",sum)
reverse()
