M, D = map(int, input().split())

# Please write your code here.
months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def month_check(m,d):
    if m>=13:
        print("No")
    else:
        if months[m]>=d:
            print("Yes")
        else:
            print("No")

month_check(M,D)