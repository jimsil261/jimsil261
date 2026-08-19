n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
square=[[0]*201 for _ in range(201)]
for i in range(n):
    if (i+1) % 2==0: 
        for x in range(x1[i],x2[i]):
            for y in range(y1[i],y2[i]):
                square[x+100][y+100]="B"
    else:
        for x in range(x1[i],x2[i]):
            for y in range(y1[i],y2[i]):
                square[x+100][y+100]="R"
count=0
for x in range(201):
    for y in range(201):
        if square[x][y]=="B":
            count+=1
print(count)