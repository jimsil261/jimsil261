word1 = input()
word2 = input()

# Please write your code here.
l_word1=list(word1)
l_word2=list(word2)
l_word1.sort()
l_word2.sort()
ans="Yes"
if len(l_word1)==len(l_word2):
    for i in range(len(l_word1)):
        if l_word1[i]!=l_word2[i]:
            ans="No"
            break
else:
    ans="No"
print(ans)