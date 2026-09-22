n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def max_func(n):
    if n==1:
        return arr[0]
    return max(arr[n-1],max_func(n-1))

print(max_func(n))