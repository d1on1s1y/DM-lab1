N1=int(input("введіть число "))

N2=0
while N1>0:
    digit=N1%10
    N1= N1//10
    N2=N2*10 +digit
    print(N2)