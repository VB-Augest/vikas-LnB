L=[]
for i in range (5):
    x=int(input("enter no-"))
    L.append(x)
print("Numbers you entered:",L)
K = [x for x in L if int(x) >9]
print("removed number less then 9: ",K)
print("sum of the remaining Numbers: ",sum(K))
