n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Please write your code here.
# Please write your code here.

students.sort(key=lambda x: (x[0], -x[1]))

for student in students:
    print(student[0], student[1], student[2])