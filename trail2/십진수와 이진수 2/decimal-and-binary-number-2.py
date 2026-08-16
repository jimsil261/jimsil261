binary=list(map(int,input()))
num=0
for i in range(len(binary)):
    num=num*2+binary[i]

num=num*17
ans=[]
while num>0:
    ans.append(num%2)
    num=num//2
print("".join(map(str,ans[::-1])))