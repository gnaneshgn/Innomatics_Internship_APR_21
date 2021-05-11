if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    data_list=[]
    list_comprehension=[[d1,d2,d3]  for d1 in range(0,x+1) for d2 in range(0,y+1) for d3 in range(0,z+1) if d1+d2+d3!=n]
    # for d1 in range(0,x+1):
    #     for d2 in range(0,y+1):
    #         for d3 in range(0,z+1):
    #             if d1+d2+d3!=n:
    #                 data_list.append([d1,d2,d3])