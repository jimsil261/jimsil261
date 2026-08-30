n, m = map(int, input().split())
A = list(map(int, input().split()))

def _return():
    global m

    total = 0

    while True:
        total += A[m - 1]

        if m == 1:
            break

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1

    return total

ans = _return()

print(ans)