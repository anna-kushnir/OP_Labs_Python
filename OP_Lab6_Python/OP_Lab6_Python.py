def factorial(i):
    if i==0:
        return 1
    else:
        f=1
        while i>=1:
            f=f*i
            i=i-1
        return f

def triangle(n):
    for i in range(0,n+1,1):
        k=i
        for j in range(0,k+1,1):
            C=int(factorial(i)/(factorial(j)*factorial(i-j)))
            print(C, end=' ')
        print(end='\n')

n=int(input("Enter the value of n: "))
print("The Pascal's triangle: ")
triangle(n)

