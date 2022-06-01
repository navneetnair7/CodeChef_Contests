t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x == y:
        print(0)
    elif y == x + 1 or x == y + 2:
        print(1)
    else:
        diff = abs(x - y)
        if diff % 2 == 0:
            print(diff // 2)
        else:
            rem = diff % 3
            q = diff // 3
            if rem == 0:
                print(q)
            else:
                print(q + 1)