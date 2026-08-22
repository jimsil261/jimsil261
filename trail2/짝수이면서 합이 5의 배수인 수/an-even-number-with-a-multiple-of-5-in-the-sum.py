n = int(input())

# Please write your code here.
def even_5(n):
    if n%2!=0:
        print("No")
    else:
        sum=0
        while n>=10:
            sum+=n%10
            n=n//10
        sum+=n
        if sum%5==0:
            print("Yes")
        else:
            print("No")

even_5(n)