name = bool(input("Введіть своє ім'я "))
surname = input("Введіть своє прізвище ")
phone = input("Введіть свій номер телефону ")

while name == False:
    name = str(input("Не залишайте поля порожніми. Введіть своє ім'я "))
while surname == False:
    surname = str(input("Не залишайте поля порожніми. Введіть своє прізвище " ))
while phone == False:
    phone = str(input("Не залишайте поля порожніми. Введіть свій номер телефону "))

print("Дякую")