# 7284 sec -> 2 hrs 1 min 24 sec
sec = int(input())
hrs = sec // 3600
b = sec - hrs * 3600
min = b // 60
sec = b - min * 60
print(f"{hrs} hrs {min} min {sec} sec")
