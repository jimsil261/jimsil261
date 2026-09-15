n = int(input())

# Please write your code here.
def printing(n):
    if n==0:
        return
    print("* "*n)
    printing(n-1)
    print("* "*n)

printing(n)