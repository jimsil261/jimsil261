a, b = map(int, input().split())

# Please write your code here.
count=0
for i in range(a,b+1,1):
    if i%3==0:
        count+=1
    else:
        num=i
        while num>0:
            if num%10==3 or num%10==6 or num%10==9:
                count+=1
                break
            else:
                num=num//10
print(count)
