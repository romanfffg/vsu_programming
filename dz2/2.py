x = input()

lst = []

while x: 

    lst.append(x)
    
    x = input()
    
lst = sorted(lst, reverse=True)

print(''.join(lst))
