# rows -> outer loop, columns -> inner loop
n = int(input())
for i in range(0, n):
    for j in range(0, n):
        print("*", end=" ")
    print("")
