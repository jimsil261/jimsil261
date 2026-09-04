n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.

# 원점과의 거리 오름차순
# 거리가 같으면 번호 오름차순
points.sort(key=lambda p: (abs(p[1][0])+abs(p[1][1]), p[0]))


for point in points:
    print(point[0]+1)