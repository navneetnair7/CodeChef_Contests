t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    b = input()
    l = []
    for i in range(n):
        if a[i] != b[i] and b[i] not in l:
            l.append(b[i])
    print(len(l))