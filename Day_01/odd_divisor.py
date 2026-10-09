# Codeforces 1475A - Odd Divisor
# keep dividing n by 2 while even, left value > 1 -> YES else NO
n = int(input())
while n % 2 == 0:
    n //= 2
if n > 1:
    print("YES")
else:
    print("NO")
