N,B=map(int,input().split())
ans=[]
while N>0:
    ans.append(N%B)
    N=N//B
print("".join(map(str,ans[::-1])))