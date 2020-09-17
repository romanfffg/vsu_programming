lst = input().split()

dct = dict.fromkeys(lst,0)

for a in lst:

    n = lst.count(a)

    dct[a] = n

print(dct)
