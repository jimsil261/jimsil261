A,B=map(int,input().split())
N=list(map(int,input()))
num=0
for i in range(len(N)):
    num=num*A+N[i]
ans=[]
while num>0:
    ans.append(num%B)
    num=num//B
print("".join(map(str,ans[::-1])))