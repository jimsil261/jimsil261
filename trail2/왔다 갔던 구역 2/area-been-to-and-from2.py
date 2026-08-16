n=int(input())
commands=[list(map(str,input().split())) for _ in range(n)]
arr=[0]*2001
current=1000
for i in range(n):
    x,d=commands[i]
    x=int(x)
    if d=="R" :
        for j in range(current,current+x,1):
            arr[j]+=1
        current+=x
    else:
        for j in range(current-1,current-x-1,-1):
            arr[j]+=1
        current-=x
count=0
for i in range(len(arr)):
    if arr[i]>=2:
        count+=1
print(count)