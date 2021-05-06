n = int(input())
s = set(map(int, input().split()))
no_of_operations=int(input())
for i in range(no_of_operations):

    op_name=input().split()
    if op_name[0]=="remove":
        if int(op_name[1]) in s:
            s.remove(int(op_name[1]))
    elif op_name[0]=="discard":
        if int(op_name[1]) in s:
            s.discard(int(op_name[1]))
    elif op_name[0]=="pop":
        s.pop()
    

print(sum(s))