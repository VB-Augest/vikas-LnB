L=[]
for i in range (5):
    x=int(input("enter no-"))
    L.insert(i,x)
print("Numbers you entered:",L)
for b in L:
    if b<9:
        L.remove(b)
print("removed number less then 9",L)
print("sum of the remaining Numbers  ",sum(L))
