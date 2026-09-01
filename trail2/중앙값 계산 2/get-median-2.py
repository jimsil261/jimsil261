n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr2=list()
for i in range(n):
    arr2.append(arr[i])
    arr2.sort()
    if (i+1)%2==1:
        print(arr2[i//2],end=" ")