a = input("Enter any text: ")

lst = []

while a:

    lst.append(a)

    a = input()

while lst:

    for c in lst:

        n = lst.count(c)

        print(c,n)

        for l in range(n):

            lst.remove(c)
