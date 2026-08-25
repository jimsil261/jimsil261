n1, n2 = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = "No"

for i in range(n1 - n2 + 1):
    if b[0] == a[i]:
        same = True

        for j in range(n2):
            if b[j] != a[i + j]:
                same = False
                break

        if same:
            ans = "Yes"
            break

print(ans)