a = str(input("Enter the text: "))
b = int(input("Enter what is number in order: "))
c = 0
for m in a:
    if m.isdigit():
        c = c + 1
    if c == k:
        print(m)
        break
