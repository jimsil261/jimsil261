A = input()

def str_reverse(s):
    new_str = ""

    for i in s:
        new_str = i + new_str

    return new_str

_str = str_reverse(A)

ans = "Yes"

for i in range(len(A)):
    if A[i] != _str[i]:
        ans = "No"
        break

print(ans)