# take a comma separated list as input
# 1. sum of all elements  2. alternate elements  3. reverse order
a = list(map(int, input().split(",")))

s = 0
for i in range(len(a)):
    s = s + a[i]
print(s)

for i in range(0, len(a), 2):
    print(a[i], end=" ")
print()

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")
