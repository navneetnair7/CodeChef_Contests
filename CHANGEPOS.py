t = int(input())
for i in range(t):
    s1, s2, e1, e2 = map(int, input().split())
    if s1 == e1:
        if s2 == e2:
            print(0)
        else:
            print(2)
    elif s2 == e2:
        print(2)
    elif s1 == e2:
        print(1)
    elif s2 == e1:
        print(1)
    else:
        print(1)