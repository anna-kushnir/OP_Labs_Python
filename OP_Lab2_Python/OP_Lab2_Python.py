print("Введіть координати вектора a (x;y;z):")
a1=float(input("a1 = ")); 
a2=float(input("a2 = ")); 
a3=float(input("a3 = "))
print("Введіть координати вектора b (x;y;z):")
b1=float(input("b1 = ")); 
b2=float(input("b2 = ")); 
b3=float(input("b3 = "))
if (b1!=0)and(b2!=0)and(b3!=0):
    if (a1/b1==a2/b2)and(a2/b2==a3/b3):
        print("Вектори a і b колінеарні");
    else:
        print("Вектори a і b не є колінеарними");
else:
    if ((a1==0)and(a2==0)and(a3==0)) or ((b1==0)and(b2==0)and(b3==0)) or ((a1==b1)and(a2==b2)and(a3==b3)):
        print("Вектори a і b колінеарні");
    else:
        print("Помилка. Введіть інші координати вектора b")