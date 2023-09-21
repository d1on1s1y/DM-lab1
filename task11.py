a = int(input("Введіть число для того щоб дізнатися чи воно просте "))
while a<=1: 
    a = int(input("Число має бути быльше ніж 1! "))
def is_it_sipmle_value(n):
    count = 0
    for i in range(1, n, 1):
        if n % i == 0:
            count+=1
    if(count == 1):
        print("Це число просте")
    else:
        print("Це число не просте")
    
is_it_sipmle_value(a)
    