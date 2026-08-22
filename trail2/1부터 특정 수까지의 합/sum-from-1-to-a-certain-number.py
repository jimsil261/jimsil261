n = int(input())

# Please write your code here.
def sum_to_n(n):
    sum=0
    for i in range(1,n+1,1):
        sum+=i
    return sum//10

print(sum_to_n(n))
