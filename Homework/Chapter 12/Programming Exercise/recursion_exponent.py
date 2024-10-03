def pp():
    
    x = int(input("What number will be the base?: "))
    y = int(input("What power do you want to raise it to?: "))
    print()
    result = 1
    
    for i in range(0, y):
        
        result *= ex(x,y)
        
    print(x, "to the power of", y, "is:" ,result)
    
    
def ex(x,y):
    total = 1
    if y == 1:
        return x
    
    elif y == 0:
        return 1
    
    else:
        y -= 1
        total *= ex(x,y)
        return total
        
pp()