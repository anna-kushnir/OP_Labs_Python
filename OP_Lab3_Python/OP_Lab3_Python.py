x=float(input("Введіть значення x: "))
n=1
a=x/2
Sum=a
while n<11:
    n=n+1
    a=(a*x)/(2*n*(2*n-1))
    Sum=Sum+a;
while abs(a)>=0.00001:
    n=n+1
    a=(a*x)/(2*n*(2*n-1))
    Sum=Sum+a;
print("Сума k членів послідовності, які задовольняють умову: %.5f" % (Sum))
