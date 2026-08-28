a, b = map(int, input().split())

# Please write your code here.
def calc(a,b):
    if a>b:
        a,b=a+25,b*2
    else:
        a,b=a*2,b+25
    return a,b
a,b=calc(a,b)
print(a,b)