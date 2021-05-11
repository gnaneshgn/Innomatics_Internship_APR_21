group_size=int(input())
group_of_people=input().split()
group_of_people_set=set(group_of_people)
group1=set()
group2=set()

for  i in group_of_people:
	if i in group1:
		group2.add(i)
	else:
		group1.add(i)

diff=list(group1.difference(group2))
print(diff[0])


