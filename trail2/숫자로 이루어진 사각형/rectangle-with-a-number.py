n = int(input())

# Please write your code here.
def print_rectangle(n):
    current=0
    for i in range(n):
        for j in range(n):
            if j!=n-1:
                print(current % 9 + 1,end=" ")
                current+=1
            else:
                print(current % 9 + 1)
                current+=1

print_rectangle(n)
