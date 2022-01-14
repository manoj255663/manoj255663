def av():
    sub1=int(input("Maths ="))
    sub2=int(input("Chem ="))
    sub3=int(input("Phy ="))
    sub4=int(input("Hindi ="))
    sub5=int(input("English ="))
    avg=(sub1+sub2+sub3+sub4+sub5)/5
    if(avg>90):
        print("A+ grade")
    elif(avg>80):
        print("A grade ")
    elif(avg>70):
        print("B+ grade ")
    elif(avg>60):
        print("B grade ")
    elif(avg>50):
        print("C+ grade ")
    elif(avg>40):
        print("c grade ")
    else:
        print("Fail")
    
av()
