# check from 2 to n-1, if n % i == 0 -> not prime
# no break -> prime (for-else)
# no need to check till n, root n is enough
n = int(input())
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")
