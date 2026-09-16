a,b=map(int,input().split())
if a<b:
    x=1
else:
    x=-1
for i in range(a,b+x,x):
    for k in range(1,4):
        if k*i<10:
            print(f"{i} * {k} =  {i*k}",end="   ")
        else:
            print(f"{i} * {k} = {i*k}",end="   ")
    print()
    for l in range(4,7):
        if l*i<10:
            print(f"{i} * {l} =  {i*l}",end="   ")
        else:
            print(f"{i} * {l} = {i*l}",end="   ")
    print()
    for m in range(7,10):
        print(f"{i} * {m} = {i*m}",end="   ")
    print()
    print()
