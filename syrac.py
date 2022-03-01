u = int(input("enter your number:" ))
while u != 1:
    if u % 2 == 0:
        u = u / 2
    else:
        u = (3 * u) +1
    print(u)