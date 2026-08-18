n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []

for num, direction in commands:
    x.append(int(num))
    dir.append(direction)


arr = [[0, 0] for _ in range(200001)]
last = [""] * 200001

current = 100000

for i in range(n):
    xi = x[i]
    diri = dir[i]

    if diri == "R":
        for j in range(xi):
            arr[current][1] += 1
            last[current] = "b"

            if j != xi - 1:
                current += 1

    else:
        for j in range(xi):
            arr[current][0] += 1
            last[current] = "w"

            if j != xi - 1:
                current -= 1

white_count = 0
black_count = 0
gray_count = 0

for i in range(len(arr)):
    white = arr[i][0]
    black = arr[i][1]

    if white >= 2 and black >= 2:
        gray_count += 1
    elif last[i] == "w":
        white_count += 1
    elif last[i] == "b":
        black_count += 1

print(white_count, black_count, gray_count)
