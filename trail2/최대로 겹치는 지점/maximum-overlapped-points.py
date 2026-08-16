n=int(input())
section=[list(map(int,input().split())) for _ in range(n)]
arr=[0]*101
for i in range(n):
    s,e=section[i]
    for j in range(s,e+1):
        arr[j]+=1
print(max(arr))