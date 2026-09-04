n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


people = []

for i in range(5):
    people.append(
        Person(name[i], height[i], weight[i])
    )


# 이름 기준 오름차순
people.sort(key=lambda x: x.name)

# 문제의 출력 형식에 맞게 출력
print("name")
for person in people:
    print(person.name,person.height,person.weight)


print()


# 키 기준 내림차순
people.sort(key=lambda x: x.height,reverse=True)
print("height")
for person in people:
    print(person.name,person.height,person.weight)