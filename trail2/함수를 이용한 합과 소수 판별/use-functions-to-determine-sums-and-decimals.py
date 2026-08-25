a, b = map(int, input().split())
count=0
for num in range(a, b + 1):
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        n=0
        while num>0:
            n+=num%10
            num//=10
        if n%2==0:
            count+=1
print(count)
