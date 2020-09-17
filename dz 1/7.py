a = int(input())

b = int(input())

c = 0

for s in range(a, b + 1):

    if not s % 5:
    
        c += s
        
print(c)
