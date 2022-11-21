n=int(input("enter a number"))
n=abs(n)
s=''
if n<0:
    n=-n
else:
    n=n
if n<3:
    print(str(n))
while n!=0:
    s=str(n%3)+s
    n=n//3
print(int(s))
