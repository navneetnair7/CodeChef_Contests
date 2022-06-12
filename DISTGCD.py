import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = abs(a - b)
    if c == 1:
        print(1)
    else:
        count = 0
        n = int(math.sqrt(c))
        r = 0
        for j in range(1, n):
            if c % j == 0:
                if c // j == j:
                    r += 1
                    count += 1
        count *= 2
        if r == 1:
            count -= 1
        print(count)