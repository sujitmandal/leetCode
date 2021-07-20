s = 'cbbd'

Substring = {}
i = 0 

for j in range(len(s)):
    if s[j] in Substring:
        i = max(i, Substring[s[j]] + 1)
    Substring[s[j]] = j

print(Substring)
a = ''  
for j in Substring:
    a = a + j
print(a)                