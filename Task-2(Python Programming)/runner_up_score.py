if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    arr = list(s)
    max_score=arr.sort()
    print(arr[-2])