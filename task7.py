import sys
def xy_input():
    xy=[int(input("Введіть значення x ")), int(input("Введіть значення y "))]
    while (xy[0] < 1 or xy[0] > 8 or xy[1] < 1 or xy[1] > 8):
        if xy[0] < 1 or xy[0] > 8:
            xy[0] = int(input("Помилка! Значеняя x має бути від 1 до 8 "))
        if xy[1] < 1 or xy[1] > 8:
            xy[1] = int(input("Помилка! Значеняя y має бути від 1 до 8 "))
    print("Координати клітинки такі ", xy)
    return xy
xy1 = xy_input()
xy2 = xy_input()
if(xy1 == xy2):
    print("Хаха, ферзь просто стоятиме, тепер введіть координати нормально")
    sys.exit()
if((abs(xy1[0]-xy2[0]) == abs(xy1[1]-xy2[1])) or (any(c1 == c2 for c1, c2 in zip(xy1, xy2)))):
    print("Ферзь може пройди з клітинки ", xy1," до клітинки ",xy2)
else:
    print("Ферзь не може пройди з клітинки ", xy1," до клітинки ",xy2)