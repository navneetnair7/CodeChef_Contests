t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        if a[-1] == 0:
            deg = 0
            for j in range(n - 1):
                if a[j] != 0 and j > deg:
                    deg = j
            print(deg)
        else:
            print(n - 1)