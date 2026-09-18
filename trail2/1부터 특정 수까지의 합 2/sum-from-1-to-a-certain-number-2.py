N = int(input())

# Please write your code here.
def add_num(n):
    if n==0:
        return 0

    return n + add_num(n-1)

print(add_num(N))