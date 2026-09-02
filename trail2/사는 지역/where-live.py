n = int(input())
name = []
address = []
region = []

for _ in range(n):
    name_value, address_value, region_value = input().split()
    name.append(name_value)
    address.append(address_value)
    region.append(region_value)

# Please write your code here.

class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
people=[]
for i in range(n):
    people.append(Person(name[i],address[i],region[i]))

last_index = 0

for i in range(1, n):
    if people[i].name > people[last_index].name:
        last_index = i

print("name",people[last_index].name)
print("addr",people[last_index].address)
print("city",people[last_index].region)

