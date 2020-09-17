import random

x = -1 #romzan

m = random.randint(0,100)

while x != m:

    x = int(input("Enter the number: "))
    
    if x == m:
    
        print("Right!")
        
    elif x > m:
    
        print("Less!")
        
    else:
    
        print("More!")
