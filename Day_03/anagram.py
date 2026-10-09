# anagram -> same letters with same length
s = input()
t = input()
freq = {}
f = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1
for j in t:
    f[j] = f.get(j, 0) + 1
if freq == f:
    print("anagram")
else:
    print("not anagram")
