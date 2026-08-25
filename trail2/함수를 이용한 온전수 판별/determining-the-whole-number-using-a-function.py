a, b = map(int, input().split())

# Please write your code here.
def check_num(n):
    cnt=0
    if n %2==0:
        cnt+=1
    elif n%5 ==0:
        cnt+=1
    elif n%3==0 and n%9!=0:
        cnt+=1

    if cnt==0:
        return True
    else:
        return False

ans=0
for i in range(a,b+1,1):
    if check_num(i)==True:
        ans+=1
print(ans)