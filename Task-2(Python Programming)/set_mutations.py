count=int(input())
values = set(map(int, input().split()))
other_sets=int(input())
for i in range(other_sets):
	operation,value=input().split()
	values2=set(map(int, input().split()))
	if operation=="intersection_update":
		values.intersection_update(values2)
		print("intersection_update:-",values)
	elif operation=="update":
		values.update(values2)
		print("update:-",values)
	elif operation=="symmetric_difference_update":
		values.symmetric_difference_update(values2)
		print("symmetric_difference_update:-",values)
	elif operation=="difference_update":
		values.difference_update(values2)
		print("difference_update:-",values2)


print(sum(values))