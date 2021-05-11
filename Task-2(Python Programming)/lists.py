f __name__ == '__main__':
    N = int(input())
values_list=[]
l=[]
i=0
while i<N:
    
    values=input()
    values_list=values.split(" ")
    if values_list[0]=="append":
        
        l.append(int(values_list[1]))
    elif values_list[0] == "insert":
            l.insert(int(values_list[1]), int(values_list[2]))
    elif values_list[0] == "remove":
            l.remove(int(values_list[1]))
    elif values_list[0] == "pop":
            l.pop()
    elif values_list[0] == "sort":
            l.sort()
    elif values_list[0] == "reverse":
            l.reverse()
    elif values_list[0] == "print":
            print(l)


    

    i+=1
    