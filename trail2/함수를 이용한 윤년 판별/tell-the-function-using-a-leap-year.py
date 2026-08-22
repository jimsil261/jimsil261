y = int(input())

# Please write your code here.
def is_yoon(n):
    if n%4==0:
        if n%100==0 and n%400!=0:
            return "false"
        else:
            return "true"
    else:
        return "false"
res=is_yoon(y)
print(res)