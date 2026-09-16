while True:
    a,b=map(int,input().split())
    if not (1<a<10 and 1<b<10):
        print("INPUT ERROR!")
    else:
        break

if a<b:
    x=1
else:
    x=-1
for i in range(a,b+x,x):
    for k in range(1,10):
        print(f"{i} * {k} = {i*k}")
    print()
