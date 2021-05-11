set_a=set(map(int, input().split()))
other_sets=int(input())
bool_value=[]
for i in range(other_sets):
	b = set(map(int, input().split()))
	length=len(b.intersection(set_a))
	if length<len(b):
		print("False")
		exit()
print("True")