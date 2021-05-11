if __name__ == '__main__':
    name_score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name,float(score)])
        second_one = sorted(list(set([marks for name, marks in name_score_list])))
sorted_list=sorted(name_score_list)
for one,two in sorted_list:
    if two==second_one[1]:
        print(one)
    else:
        pass