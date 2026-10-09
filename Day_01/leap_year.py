# divisible by 400 or (divisible by 4 and not divisible by 100)
year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not a leap year")
