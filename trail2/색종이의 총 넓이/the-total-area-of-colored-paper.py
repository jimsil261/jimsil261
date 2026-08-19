n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
square=[[0]*201 for _ in range(201)]
for i in range(n):
    for a in range(x[i],x[i]+8,1):
        for b in range(y[i],y[i]+8,1):
            square[a+100][b+100]=1
count=0
for a in range(201):
    for b in range(201):
        if square[a][b]==1:
            count+=1
print(count)