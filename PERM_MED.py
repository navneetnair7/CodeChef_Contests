from tkinter import N


t = int(input())
for i in range(t):
    n = int(input())
    z = 1
    n1 = n
    for i in range(n):
        if i % 2 == 0:
            print(n1, end = ' ')
            n1 -= 1
        else:
            print(z, end = ' ')
            z += 1
    print()