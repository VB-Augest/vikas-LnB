a=int(input("Enter a value:"))
b=int(input("Enter 2nd value:"))
c=int(input("Enter 3rd value:"))
d=int(input("Enter 4th value:"))
e=int(input("Enter 5th value:"))
List= [a,b,c,d,e]
print(List)
if(a<=9):
    List.remove(a)
if(b<=9):
    List.remove(b)
if(c<=9):
    List.remove(c)
if(d<=9):
    List.remove(d)
if(e<=9):
    List.remove(e)
print(sum(List))
