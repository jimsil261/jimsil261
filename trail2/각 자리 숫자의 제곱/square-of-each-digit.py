N = int(input())

# Please write your code here.
def sum_pow(n):
    if n==0:
        return 0
    return (n%10) ** 2 + sum_pow(n//10)
print(sum_pow(N))