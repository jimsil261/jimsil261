n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def to_abs(arr):
    for i in range(len(arr)):
        arr[i]=abs(arr[i])
    return arr
arr=to_abs(arr)
print(*arr)
        