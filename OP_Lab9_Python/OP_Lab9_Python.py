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
    Max=words[0]
    Min=words[0]
    nMax=nMin=0
    for i in range(1,len(words),1):
        if int(words[i])>int(Max):
            Max=words[i]
            nMax=i
        if int(words[i])<int(Min):
            Min=words[i]
            nMin=i
    print("The biggest word is number ",nMax+1,": ",Max)
    print("The smallest word is number ",nMin+1,": ",Min)
    s=replace(s,words,nMax,nMin)
    print("New string:",s)
else:
    print("You entered a wrong line!")



