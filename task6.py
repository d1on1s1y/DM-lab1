x = int(input("Введіть значення x "))
y = int(input("Введіть значення y "))

#if (x < 1 or x > 8 or y < 1 or y > 8):
while (x < 1 or x > 8 or y < 1 or y > 8):
    if x < 1 or x > 8:
        x = int(input("Помилка! Значення x має бути від 1 до 8 "))
    if y < 1 or y > 8:
        y = int(input("Помилка! Значення y має бути від 1 до 8 "))
if (x + y)%2 == 0:
    print("Клітинка чорна")
else:
    print("Клітинка біла")