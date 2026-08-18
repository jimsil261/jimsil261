n=int(input())
commands=[list(map(str,input().split())) for _ in range(n)]

arr=[0]*200001
current=100000
for i in range(n):
    x,dir=commands[i]
    x=int(x)
    if dir=="L":
        for j in range(x):
            arr[current]=1
            if j != x-1:
                current-=1
    else:
        for j in range(x):
            arr[current]=2
            if j != x-1:
                current+=1
count=[0]*2
for i in range(len(arr)):
    if arr[i]==1:
        count[0]+=1
    elif arr[i]==2:
        count[1]+=1
print(*count)