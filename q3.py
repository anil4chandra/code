def patrol(b) :
	for i in range(len(b)) :
		if (b[i] == '4' or b[i] == '6' or b[i] == '7') :
			return False;
	return True;

g=int(input())
count=0
l=[]
for i in range(1,1000000):
    if (patrol(str(i))) :
        count+=1
        l.append(i)
print(l[g-1])
