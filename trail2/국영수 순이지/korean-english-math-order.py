n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math


students = []

for i in range(n):
    students.append(
        Student(name[i], korean[i], english[i], math[i])

    )


# 국어 → 영어 → 수학 우선순위로 내림차순 정렬
students.sort(key=lambda x: (x.korean, x.english, x.math),reverse=True)


for student in students:
    print(student.name, student.korean, student.english, student.math)