x="chetan"
print(x)
x="chetan\rsunhare"
print(x)
x="chetan\tsunhare"
print(x)
x="chetan\nsunhare"
print(x)
x="chetan\bsunhare"
print(x)
x="chetan"
print(len(x[2:]))
print(x.index("t"))
print(x.upper())
print(x.lower())
print(x.capitalize())
x="chetan Sunhare 23 gg"
def count():
    c=0
    for w in range(len(x)):
        if(x[w].isspace()):
            c=c+1
    print(c+1)
count()
        
