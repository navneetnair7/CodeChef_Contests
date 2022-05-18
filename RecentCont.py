t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    s = 0
    l = 0
    for i in a:
        if len(i) == 7:
            s += 1
        else:
            l += 1
    print(s, l)