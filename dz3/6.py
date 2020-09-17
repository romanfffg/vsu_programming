def retorn(ch):

    a = 2

    while not (ch % a == 0):

        a += 1

    if a == ch:

        return "True"

    else:

        return "False"

 b= int(input("Enter your number: "))

print(retorn(b))
