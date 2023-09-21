a = int(input("Ведіть число a "))
b = int(input("Ведіть число b "))
c = int(input("Ведіть число c "))
numbers = [a, b, c]
if(a < b and b < c):
    print("Рівність a < b < с виконуєься")
else:
    print("Рівність a < b < с не виконуєься")

if any(x > 0 for x in numbers):
    print("Мінімум одне з чисел є додатнім")
else:
    print("Усі числа від'ємні")
i=0
for num in numbers:
    if(num < 0):
        i=+1

if i == 1:
    print("Серед чих чисел тільки одне від'ємне")
else:
    print("Серед цих чисел немає, або більше ніж одне від'ємне")