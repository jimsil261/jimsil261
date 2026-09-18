N = int(input())

# Please write your code here.
def func(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + func(n/2)
    else:
        return 1 + func(n//3)

print(func(N))