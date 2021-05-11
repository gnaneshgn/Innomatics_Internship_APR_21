if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    temp=0
    named_values=list(student_marks.get(query_name))
    for i in range(0,len(named_values)):
        temp=temp+named_values[i]
    avg=temp/len(named_values)
    print("{0:.2f}".format(float(avg)))