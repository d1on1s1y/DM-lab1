a = int(input("Введіть менше число "))
b = int(input("Введіть більше число "))
while b <= a :
    b = int(input("Друге число має бути більшим! "))
i = a
while i <= b :
    print (i)
    i+=1
print("Виведено ",b-a+1," чисел")