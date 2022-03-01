x = int(input("enter your number:" ))
y = int(input("enter your number:" ))
compt = 0
answer = 0
while x != 0:
    compt = compt +1
    if x % 2 == 1:
        answer = answer + y
    x = x // 2
    y = y *2
print("nombre d'iteration:" ,compt)
print("the answer is :",answer)