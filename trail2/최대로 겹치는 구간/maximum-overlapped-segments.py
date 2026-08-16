n = int(input())
section = [list(map(int, input().split())) for _ in range(n)]

arr = [0] * 201

for i in range(n):
    s, e = section[i]

    for j in range(100+s,100+e):
        arr[j]+=1

print(max(arr))