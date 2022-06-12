t = int(input())
for i in range(t):
    n = int(input())
    p = []
    if n == 2:
        print(1, 2)
    else:
        if n % 2 == 0:
            p.append(n // 2)
            for i in range(1, n):
                if i % 2 == 0:
                    p.append(p[i - 1] - i)
                else:
                    p.append(p[i - 1] + i)
        else:
            p.append(n // 2 + 1)
            for i in range(1, n):
                if i % 2 == 0:
                    p.append(p[i - 1] + i)
                else:
                    p.append(p[i - 1] - i)
        for i in range(n):
            print(p[i], end=' ')