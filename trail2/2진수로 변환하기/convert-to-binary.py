N=int(input())
ans=[]
while N>=2:
    ans.append(N%2)
    N=N//2
ans.append(N)
print("".join(map(str,ans[::-1])))
