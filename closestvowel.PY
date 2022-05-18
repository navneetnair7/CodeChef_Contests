t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    t = 1
    for i in range(n):
        if s[i] == 'c' or s[i] == 'g' or s[i] == 'l' or s[i] == 'r':
            t = t * 2
    print(t % 1000000007)