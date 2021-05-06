dim1,dim2=map(int,input().split())
l=list(map(int,input().split()))
a=input().split()
a_set=set(map(int,a))
b=input().split()
b_set=set(map(int,b))

new_set=a_set | b_set

datt_l=[]
value=0

for i in l:
	if i in new_set:
		datt_l.append(i)

for d in datt_l:
	if d in a_set:
		value+=1
	else:
		value-=1
print(value)

