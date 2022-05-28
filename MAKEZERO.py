def check(lst):
    if lst == []:
        return False
    else:
        return True


def remove0(lst):
    a = lst.count(0)
    for i in range(a):
        lst.remove(0)


def max_power_of_2(x):
    a = 0
    while True:
        if 2**a > x:
            return a-1
            break
        else:
            a += 1

def main():
    t=int(input())
    cases=[]
    for i in range(t):
        a=int(input())
        lst=list(map(int, input().split()))
        cases.append(lst)

    for lst in cases:
        lst = set(lst)
        lst = list(lst)
        remove0(lst)
        count = 0

        while check(lst):
            
            odd_check = False
            for i in range(len(lst)):
                if lst[i] % 2 == 1:
                    lst[i] -= 1
                    odd_check = True
            if odd_check:
                count += 1
                remove0(lst)

            if len(lst)>1:
                dup_lst = lst.copy()
                dup_lst.remove(min(lst))
                xyz = min(dup_lst)
            elif len(lst)==1:
                count+=1
                break
            else:
                break
            
            for i in range(len(lst)):
                if lst[i] >= xyz:
                    lst[i] -= xyz
            count += 1
            remove0(lst)
        print(count)
main()