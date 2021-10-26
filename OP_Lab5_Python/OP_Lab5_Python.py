m=int(input("Введіть значення m: "))
n=int(input("Введіть значення n: "))
for k in range(1,m,1):
    Sum_k=0
    i=k
    while i>0:
       Sum_k=Sum_k+i%10
       i=i//10
    if Sum_k==n:
       print(k)