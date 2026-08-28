a, b = map(int, input().split())

# Please write your code here.
def change(a,b):
    if a>b:
        a,b=a*2,b+10
    else:
        a,b=a+10,b*2
    return a,b
a,b=change(a,b)

print(a,b)