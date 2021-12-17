#Заданий рядок символів, що містить цифри і пробіли.
#Групи цифр, що розділені пробілами (одним або декількома), вважаємо словами. 
#Розглядаючи кожне слово як число, визначити найбільше і найменше із них і поміняти знайдені слова місцями.

def check(str):
    R=0
    for i in range(0,len(str),1):
        c=str[i]
        if c.isdigit() or c.isspace():
            R=1
        else:
            R=0
            break
    return R

def output(st):
    for i in range(0,len(st),1):
        print(st[i], end='\n')

def search_Max(st):
    max=st[0]
    for i in range(1,len(st),1):
        if int(st[i])>int(max):
            max=st[i]
            numMax=i
    return numMax

def search_Min(st):
    for i in range(1,len(st),1):
        if int(st[i])<int(min):
            min=st[i]
            numMin=i
    return numMin

def replace(str,st,numMax,numMin):
    st[numMax],st[numMin]=st[numMin],st[numMax]
    str=' '.join(st)
    return str

s=input("Input string of numbers and spaces: ")
Is=check(s)
if Is:
    words=s.split()
    print("The number of words: ",len(words))
    print("The list of words:")
    output(words)
    nMax=search_Max(words)
    nMin=search_Min(words)
    print("The biggest word is number ",nMax+1,": ",words[nMax])
    print("The smallest word is number ",nMin+1,": ",words[nMin])
    s=replace(s,words,nMax,nMin)
    print("New string:",s)
else:
    print("You entered a wrong line!")
