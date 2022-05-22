t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    count = 0
    #check if a is a palindrome
    if a == a[::-1]:
        print("YES")
    #if not a palindrome then print the minimum number of XOR operations required to make it a palindrome
    else:
        for j in range(n // 2):
            if a[j] != a[n-j-1]:
                count += 1
        print((count + 1 ) // 2)