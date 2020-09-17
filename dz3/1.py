import string

A = int()

B = int()

A_ = []

B_ = []

l = 0
lst = input()

for i in lst
:
    if i in string.punctuation:

        x = i

        c = 1

    elif c == 0:
        A_.append(i)

    else:

        B_.append(i)

A = int(''.join(A_))
 
B = int(''.join(B_))
 
if x == "+":

    print(A + B)

elif x == "*":

    print(A * B)

elif x == "-":

   print(A - B)

elif x == "%":

   print(A % B)

elif x == "**":

   print(A ** B)
elif x == "//":
   print(A // B)
elif x == "/":
   print(A / B)
