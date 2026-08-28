n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def new_arr(arr):
    new_array=list()
    for i in arr:
        if i%2==1:
            new_array.append(i)
        else:
            new_array.append(int(i/2))
    return new_array
ans=new_arr(arr)
print(*ans)