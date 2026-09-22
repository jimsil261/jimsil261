N = int(input())

# Please write your code here.
def func(n):
    if n<0:
        return 0
    return n+func(n-2)

print(func(N))