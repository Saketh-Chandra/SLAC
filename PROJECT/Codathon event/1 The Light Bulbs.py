def abc():
    t=int(input())
    a="true"
    for i in range(1,t):
        if t%i==0 and a=="true":
            a="false"
        elif t%i==0 and a=="false":
            a="true"
    
    if a=="true":
        print("yes")
    else:
         print("no")


n=int(input())
for j in range(n):
    abc()
