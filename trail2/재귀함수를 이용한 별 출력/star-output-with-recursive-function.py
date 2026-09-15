n = int(input())

# Please write your code here.
def increase_star(n):
    if n==0:
        return
    increase_star(n-1)
    print("*"*n)

increase_star(n)
