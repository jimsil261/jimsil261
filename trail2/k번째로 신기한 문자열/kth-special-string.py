n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
arr=[]
for i in range(n):
    res=1
    if len(str[i])<len(t):
        res=0
    else:
        for j in range(len(t)):
            if t[j]!=str[i][j]:
                res=0
    if res==1:
        arr.append(str[i])
arr.sort()
print(arr[k-1])