MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
min_index=0
for i in range(1,MAX_N):
    if users[i][1]<users[min_index][1]:
        min_index=i

print(*users[min_index])