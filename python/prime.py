def prime():
    x=int(input("Enter Number = "))
    i=2
    flage=0
    while i<x:
        if(x%i==0):
            flage=1
        i=i+1

    if(flage==1):
        print("Numberb is not prime")
    else:
        print("number is prime")
prime();
