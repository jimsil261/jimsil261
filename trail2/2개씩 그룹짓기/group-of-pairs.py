n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
ans=list()
for i in range(int(n)):
    ans.append(nums[i]+nums[-i-1])
print(max(ans))