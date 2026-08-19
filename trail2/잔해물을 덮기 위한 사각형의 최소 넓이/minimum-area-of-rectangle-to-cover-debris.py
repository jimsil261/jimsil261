x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Please write your code here.
square=[[0]*2001 for _ in range(2001)]
for x in range(x1[0],x2[0],1):
    for y in range(y1[0],y2[0],1):
        square[x+1000][y+1000]=1
for x in range(x1[1],x2[1],1):
    for y in range(y1[1],y2[1],1):
        square[x+1000][y+1000]=0
minx=10000
maxx=-1
miny=10000
maxy=-1
for x in range(2001):
    for y in range(2001):
        if square[x][y]==1:
            minx=min(minx,x)
            maxx=max(maxx,x)
            miny=min(miny,y)
            maxy=max(maxy,y)
if maxx== -1:
    print(0)
else:
    print((maxx-minx+1)*(maxy-miny+1))