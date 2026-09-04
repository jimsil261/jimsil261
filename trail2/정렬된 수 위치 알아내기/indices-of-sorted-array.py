n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
# (값, 원래 위치)를 저장
numbers = []

for i in range(n):
    numbers.append((sequence[i], i))


# 값이 작은 순 → 값이 같으면 원래 위치가 작은 순
numbers.sort(key=lambda x: (x[0], x[1]))


# 원래 각 원소가 정렬 후 몇 번째 위치로 갔는지 저장
answer = [0] * n

for new_index in range(n):
    original_index = numbers[new_index][1]

    answer[original_index] = new_index+1


print(*answer)