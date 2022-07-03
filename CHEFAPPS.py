t = int(input())
for i in range(t):
    s, x, y, z = map(int, input().split())
    s2 = s - x - y
    if z <= s2:
        print(0)
    else:
        r = max(x, y)
        if z <= s2 + r:
            print(1)
        else:
            print(2)