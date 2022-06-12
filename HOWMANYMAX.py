t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = []
    for i in range(n - 1):
        if s[i] == '0':
            a[i] == 0 and a[i + 1] == 1
        elif s[i] == '1':
            a[i] == 1 and a[i + 1] == 0