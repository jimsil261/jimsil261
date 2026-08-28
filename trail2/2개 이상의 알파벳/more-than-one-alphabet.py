A = input()

count = [0] * 26

def al_count(s):
    for i in s:
        index = ord(i) - ord('a')
        count[index] += 1

    return count

count = al_count(A)

ans = 0

for i in range(len(count)):
    if count[i] > 0:
        ans += 1

if ans >= 2:
    print("Yes")
else:
    print("No")