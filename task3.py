import sys
print("Введіть координати протилежних сторін прямокутника. Увага! Точки не мають лежати на прямій паралельній одній з осей координат")
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
if(x1 == x2 or y1 == y2):  
    print("Помилка. Неправильні дані")
    sys.exit()
def calculate_side(n1, n2):
    if(((n1 < 0) and (n2 > 0)) or ((n1 > 0) and (n2 < 0)) ):
        return abs(n1) + abs(n2)
    else:
        return abs(n1-n2)
x_side = calculate_side(x1,x2)
y_side = calculate_side(y1,y2)
print("Сторона паралельна осі x =", x_side)
print("Сторона паралельна осі x =", y_side)
print("Площа прямокутника = ", x_side*y_side)
print("Периметр прямокутника = ", (x_side + y_side)*2)


    