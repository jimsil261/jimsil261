text = input()
pattern = input()

# Please write your code here.
def is_match(i):
    for x in range(len(pattern)):
        if text[i+x]==pattern[x]:
            continue
        else:
            return -1
    return i

ans=-1
for i in range(len(text)-len(pattern)+1):
    if is_match(i) != -1 :
        ans=i
        break
print(ans)