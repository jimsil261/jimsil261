n = int(input())

# Please write your code here.
def increase_num(n):
    if n==0:
        return

    increase_num(n-1)
    print(n,end=" ")

def decrease_num(n):
    if n==0:
        return
    print(n,end=" ")
    decrease_num(n-1)

increase_num(n)
print("")
decrease_num(n)